# Download Intercom tickets to your Mac

Goal: a year of tickets saved in a folder on your own computer, never in a cloud or remote session.

## 1. Put the tools in a folder
Make a folder called `support-wiki-tools` in your home folder (not Desktop or Documents) and put these three files in it: `download_tickets.py`, `SETUP_MAC.md`, `LOCAL_CLAUDE_INSTRUCTIONS.md`.

## 2. Open Terminal and check Python
Open Terminal (Cmd+Space, type Terminal). Run:

    python3 --version

If macOS offers to install "Command Line Tools", accept and wait for it to finish, then run it again. Any version 3.8 or newer works. Nothing else needs installing.

## 3. Pick the data folder
The script saves to `~/support-wiki-data` by default. It refuses Desktop, Documents, iCloud Drive, Dropbox, OneDrive and Google Drive, because those sync to the cloud. Also make sure FileVault is on: System Settings > Privacy & Security > FileVault.

## 4. Get the Intercom token
In Intercom: Developer Hub > your app > Authentication. Under permissions, turn on **Read conversations** only. Turn off everything that writes, and leave contacts and companies off. Save the permissions, then click **Regenerate** next to the access token so the new token carries the saved settings (Intercom shows a warning about "outdated permissions" until you do). Copy the new token into your password manager. When you are done with the project, revoke it.

Paste it into Terminal so it never appears in a chat, a file, or your command history:

    read -s "INTERCOM_TOKEN?Paste token, then press Return: "
    export INTERCOM_TOKEN

(Nothing shows as you paste. That is normal.) If your Intercom workspace is in the EU or Australia, also run `export INTERCOM_REGION=eu` or `au`.

## 5. Test with 20 tickets
    cd ~/support-wiki-tools
    python3 download_tickets.py --limit 20

It prints this computer's name and the save folder and asks you to confirm. Then open `~/support-wiki-data/slim` in Finder and read a few files. Check they look right: customer and agent turns in order, readable text, tags present.

## 6. Run the full year
    python3 download_tickets.py

It can be stopped with Ctrl+C and re-run; it skips tickets it already saved. Expect it to take a while (about 9,000 tickets, one request each). When it finishes, `~/support-wiki-data/manifest.json` shows the counts. If "possibly_truncated" is above 0, tell Claude.

## 7. Start a local Claude Code session
Install Claude Code on your Mac (the desktop app or the terminal version from claude.com/claude-code) and open a **local** session in `~/support-wiki-tools`, not a web or cloud session. Verify by asking it to run `pwd` and `hostname`: a path starting `/Users/<you>/` means local. Paste the contents of `LOCAL_CLAUDE_INSTRUCTIONS.md` as your first message. Start in a restrictive permission mode so it asks before reading files or running commands.

## 8. When you're done
Keep `~/support-wiki-data` only as long as the project needs it, then delete it. Don't copy it anywhere else, and don't attach it to email, Slack, Notion or Drive.
