#!/usr/bin/env python3
"""Download Intercom conversations to THIS computer (standard library only).

Run it on your own Mac, never in a cloud or remote session. Conversations
contain patient information, so the files stay in a local folder.

For every conversation it writes two files:
  raw/<id>.json   the full API response
  slim/<id>.txt   plain-text transcript (cheap for Claude to read)

It is resumable: conversations already in raw/ are skipped, so you can stop and
re-run at any time. Nothing from a conversation is ever printed to the screen.

The Intercom token is read from the INTERCOM_TOKEN environment variable, or
else from a plain-text file (default ~/intercom-token.txt). See SETUP_MAC.md.

Usage:
  python3 download_tickets.py --limit 20      # small test run first
  python3 download_tickets.py                  # the full last 365 days
"""
import argparse
import html
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

REGIONS = {
    "us": "https://api.intercom.io",
    "eu": "https://api.eu.intercom.io",
    "au": "https://api.au.intercom.io",
}
API_VERSION = "2.11"

# Folders that sync to the cloud. Saving patient data there would copy it off
# this computer.
SYNCED_NAMES = {
    "mobile documents", "icloud drive", "dropbox", "google drive", "googledrive",
    "onedrive", "cloudstorage", "box", "box sync",
}
# macOS can sync these two folders to iCloud ("Desktop & Documents Folders").
ICLOUD_CAPABLE = ("Desktop", "Documents")


def synced_location_reason(path: Path):
    home = Path.home().resolve()
    for part in path.parts:
        low = part.lower()
        if low in SYNCED_NAMES or low.startswith(("onedrive", "dropbox")):
            return f"'{part}' is a cloud-synced folder"
    for name in ICLOUD_CAPABLE:
        base = home / name
        if path == base or base in path.parents:
            return f"~/{name} may be synced to iCloud"
    return None


def read_token_file(path_str):
    path = Path(path_str).expanduser()
    if not path.is_file():
        return None
    reason = synced_location_reason(path.resolve())
    if reason:
        sys.exit(f"Refusing to read the token from {path}: {reason}. "
                 "Move it to your home folder, e.g. ~/intercom-token.txt.")
    if path.stat().st_mode & 0o077:
        os.chmod(path, 0o600)
        print(f"Tightened permissions on {path} so only you can read it.")
    text = path.read_text(encoding="utf-8-sig", errors="replace").strip()
    if text.startswith("{\\rtf"):
        sys.exit(f"{path} was saved as rich text. Reopen it in TextEdit, choose "
                 "Format > Make Plain Text, and save it again.")
    lines = text.splitlines()
    return lines[0].strip() if lines else None


def call(method, path, token, base, body=None, params=None):
    url = base + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Intercom-Version": API_VERSION,
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    for attempt in range(7):
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                sys.exit(f"Intercom rejected the token (HTTP {e.code}). "
                         "Check the token and that it can read conversations.")
            if e.code in (429, 500, 502, 503, 504):
                retry_after = e.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else min(2 ** attempt, 30)
                print(f"  Intercom said HTTP {e.code}; waiting {wait:.0f}s and retrying")
                time.sleep(wait)
                continue
            sys.exit(f"Intercom returned HTTP {e.code} for {method} {path}")
        except (urllib.error.URLError, socket.timeout):
            time.sleep(min(2 ** attempt, 30))
    sys.exit(f"Gave up after repeated failures on {method} {path}")


def list_ids(token, base, since_ts, limit):
    ids, cursor = [], None
    while True:
        page = {"per_page": 150}
        if cursor:
            page["starting_after"] = cursor
        body = {
            "query": {"operator": "AND",
                      "value": [{"field": "created_at", "operator": ">", "value": since_ts}]},
            "pagination": page,
        }
        res = call("POST", "/conversations/search", token, base, body=body)
        for conv in res.get("conversations", []):
            ids.append(str(conv["id"]))
        print(f"  found {len(ids)} conversations so far")
        if limit and len(ids) >= limit:
            return ids[:limit]
        nxt = (res.get("pagination") or {}).get("next") or {}
        cursor = nxt.get("starting_after")
        if not cursor:
            return ids


def iso(ts):
    if not ts:
        return "unknown"
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def clean(text):
    if not text:
        return ""
    text = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text).strip()


ROLE = {"user": "customer", "lead": "customer", "contact": "customer",
        "admin": "agent", "bot": "bot", "team": "team"}


def slim(conv):
    src = conv.get("source") or {}
    tags = ", ".join(t.get("name", "") for t in (conv.get("tags") or {}).get("tags", []))
    out = [f"id: {conv.get('id')}", f"created: {iso(conv.get('created_at'))}",
           f"state: {conv.get('state')}", f"tags: {tags}"]
    if src.get("subject"):
        out.append(f"subject: {clean(src['subject'])}")
    out.append("")
    first = clean(src.get("body"))
    if first:
        role = ROLE.get((src.get("author") or {}).get("type"), "other")
        out.append(f"[{iso(conv.get('created_at'))}] {role}: {first}")
    parts = (conv.get("conversation_parts") or {}).get("conversation_parts", [])
    for part in parts:
        body = clean(part.get("body"))
        if not body:
            continue
        if part.get("part_type") == "note":
            role = "internal note"
        else:
            role = ROLE.get((part.get("author") or {}).get("type"), "other")
        out.append(f"[{iso(part.get('created_at'))}] {role}: {body}")
    return "\n".join(out) + "\n"


def write_atomic(path: Path, text: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", help="YYYY-MM-DD (default: 365 days ago)")
    ap.add_argument("--limit", type=int, help="stop after N conversations (for test runs)")
    ap.add_argument("--out", default="~/support-wiki-data", help="output folder")
    ap.add_argument("--region", default=os.environ.get("INTERCOM_REGION", "us"),
                    choices=sorted(REGIONS))
    ap.add_argument("--token-file", default="~/intercom-token.txt",
                    help="plain-text file holding the token (used if INTERCOM_TOKEN is not set)")
    ap.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    args = ap.parse_args()

    token = os.environ.get("INTERCOM_TOKEN") or read_token_file(args.token_file)
    if not token:
        sys.exit("No Intercom token found. Save it in a plain-text file at "
                 f"{args.token_file} or set INTERCOM_TOKEN. See SETUP_MAC.md.")
    base = os.environ.get("INTERCOM_BASE_URL") or REGIONS[args.region]

    out = Path(args.out).expanduser().resolve()
    reason = synced_location_reason(out)
    if reason:
        sys.exit(f"Refusing to save to {out}: {reason}. "
                 "Choose a folder that does not sync, e.g. ~/support-wiki-data.")

    if args.since:
        since = datetime.strptime(args.since, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        since = datetime.now(timezone.utc) - timedelta(days=365)

    print(f"This computer: {socket.gethostname()}")
    print(f"Saving to:     {out}")
    print(f"Conversations created since {since.date()}"
          + (f", first {args.limit} only" if args.limit else ""))
    if not args.yes and input("Is that a folder on your own Mac? Type y to continue: ").lower() != "y":
        sys.exit("Stopped.")

    raw_dir, slim_dir = out / "raw", out / "slim"
    for d in (out, raw_dir, slim_dir):
        d.mkdir(parents=True, exist_ok=True)
        os.chmod(d, 0o700)

    print("Listing conversations...")
    ids = list_ids(token, base, int(since.timestamp()), args.limit)

    done = skipped = truncated = 0
    for i, cid in enumerate(ids, 1):
        raw_path = raw_dir / f"{cid}.json"
        if raw_path.exists():
            skipped += 1
            continue
        conv = call("GET", f"/conversations/{cid}", token, base,
                    params={"display_as": "plaintext"})
        parts = conv.get("conversation_parts") or {}
        if parts.get("total_count", 0) > len(parts.get("conversation_parts", [])):
            truncated += 1
        write_atomic(raw_path, json.dumps(conv))
        write_atomic(slim_dir / f"{cid}.txt", slim(conv))
        done += 1
        if i % 50 == 0 or i == len(ids):
            print(f"  {i}/{len(ids)} processed")

    manifest = {"since": since.date().isoformat(), "found": len(ids),
                "downloaded_this_run": done, "already_had": skipped,
                "possibly_truncated": truncated,
                "finished": datetime.now(timezone.utc).isoformat()}
    write_atomic(out / "manifest.json", json.dumps(manifest, indent=2))
    print(f"Done. {done} downloaded, {skipped} already present, "
          f"{truncated} with more parts than the API returned.")
    print(f"Files are in {out}. They contain patient information; do not move them "
          "into a synced folder, email them, or upload them anywhere.")


if __name__ == "__main__":
    main()
