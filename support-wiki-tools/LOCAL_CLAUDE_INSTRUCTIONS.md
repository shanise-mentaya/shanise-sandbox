# Instructions for my local Claude session (paste as the first message)

I'm Shanise, on the Mentaya support team. We're building a support wiki: validated answers to customer questions, plus SOPs. The plan and design decisions are in the Playbook doc: https://claude.ai/artifact/RbXFh9kRJL8YgqM3Yh9hCh (tabs: Playbook, Wiki v1 draft, Notion cleanup list). My own working version, with the decisions I made on 9/30 and a draft claim status SOP, is here: https://claude.ai/artifact/64J26LuXtfSh2eGqGCiNak. Read the Playbook tab and my working version first, and play back what we're building before doing anything else.

## First job: download a year of Intercom tickets to this Mac
I'm not comfortable in Terminal yet, so you'll run the download script and I'll approve each command.
- The script is `~/support-wiki-tools/download_tickets.py`. It saves tickets to `~/support-wiki-data`. It reads my read-only Intercom token from `~/intercom-token.txt`.
- **Never open, read, print or copy `~/intercom-token.txt` or the token itself.** Don't ask me to paste it into this chat. Don't run commands that would show it (cat, echo, env, printenv, and so on). If a run fails because of the token, tell me what the error says and I'll fix the file.
- Read the script first and tell me in plain English what it does, and whether anything in it looks unsafe.
- Run `pwd` and `hostname` and show me the output, so we both know this is my own Mac. Then tell me the save folder, `~/support-wiki-data`, and wait for me to confirm it is a normal folder on this computer.
- Run the test: `python3 ~/support-wiki-tools/download_tickets.py --limit 20 --yes`. Then open a couple of files from `~/support-wiki-data/slim` and tell me whether they read as customer and agent turns in order.
- Wait for my OK, then run the full year: `python3 ~/support-wiki-tools/download_tickets.py --yes`. This takes a long while, so run it in the background and check on it. The script is resumable: if it gets interrupted, run the same command again.
- When it finishes, read `~/support-wiki-data/manifest.json` and tell me the counts. If `possibly_truncated` is above 0, explain what that means.

## Then: the analysis
After the download, the next step is a taxonomy of the kinds of questions customers ask, drafted from about 300 tickets. Propose the plan and the cost, and wait for my OK before starting.

## Rules for patient data
- `~/support-wiki-data` holds a year of Intercom tickets, including patient information. It is fine for you to read it. It must never leave this computer.
- Don't copy, upload, email, commit or sync any of it. Don't send any of it to any connector (Slack, Notion, Linear, Drive, Gmail, Intercom notes, Metabase, anything).
- Anything you write outside `~/support-wiki-data` (the wiki, the taxonomy, the question bank, summaries to me or to others) must contain no patient or client names, dates of birth, member IDs, emails or phone numbers. Use patterns, counts and anonymized paraphrases only. If you're unsure whether something identifies someone, leave it out.
- Keep the data folder out of any git repository and out of any cloud-synced folder.

## How to work
- Read `slim/` (plain-text transcripts), not `raw/`, unless you need a field that only the raw JSON has.
- Never read the tickets one by one into this conversation. Use scripts to count and group, and have a cheaper model label tickets in batches if needed. Before any large step, tell me what you'll do, the estimated token cost and the time, and wait for my OK. Pilot on about 200 tickets and report the real cost before scaling to the full year.
- A customer's question is evidence of what people ask. An agent's reply is a claim to check, not a fact. Log answers as unvalidated with evidence (how often, how recent, whether the customer came back), and never promote one to the wiki without my confirmation.
- Ranked sources of truth: product code, then product docs, then me. Current Notion pages are leads until I confirm them. Never treat Intercom replies, archived Notion pages, old help articles or Slack threads as facts.
- Plan first: outline each step and wait for my OK before starting it.
- Explain anything I don't understand as if I'm a smart 12th grader.
