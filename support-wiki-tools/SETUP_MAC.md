# Download Intercom tickets to your Mac, using a local Claude Code session

Goal: a year of tickets saved in a folder on your own computer, never in a cloud or remote session. You won't type commands. A local Claude Code session runs the download script, and you approve each step.

## 1. Put the tools in a folder
In Finder, open your home folder (the one with your name). Make a folder called `support-wiki-tools` in it, not on Desktop or in Documents (those can sync to iCloud). Put these three files in it: `download_tickets.py`, `SETUP_MAC.md`, `LOCAL_CLAUDE_INSTRUCTIONS.md`.

## 2. Check your Mac and install Claude Code
- Make sure FileVault is on: System Settings > Privacy & Security > FileVault.
- Install the Claude Code desktop app if you haven't. Make sure it can reach Notion so it can read the Playbook doc.

## 3. Get the Intercom token and save it in a file
1. In Intercom: Developer Hub > your app > Authentication. Under permissions, turn on **Read conversations** only. Turn off everything that writes, and leave contacts and companies off. Save.
2. Click **Regenerate** next to the access token so the new token carries the saved permissions. Copy it.
3. Put the token in your password manager.
4. Open **TextEdit** (Cmd+Space, type TextEdit). Choose **Format > Make Plain Text** (Shift+Cmd+T). Paste the token and nothing else.
5. Choose **File > Save**. Name it `intercom-token.txt`. In the save window, pick the folder with your name in the sidebar (your home folder), not iCloud, Desktop or Documents. Close TextEdit.

The script tightens this file so only you can read it, and it never prints the token.

## 4. Start a local Claude Code session
Open the Claude Code desktop app. Start a **local** session with `support-wiki-tools` as the working folder, not a web or cloud session. Use a permission mode that asks before it acts. Ask it to run `pwd` and `hostname`: a path starting `/Users/` means local.

## 5. Paste the message
Open `LOCAL_CLAUDE_INSTRUCTIONS.md` and paste its whole contents as your first message. Claude will read the Playbook and your doc, play back what we're building, then walk you through the download.

## 6. During the download, you approve each command
- **Test run first.** Claude runs the script for 20 tickets after you confirm the save folder is `~/support-wiki-data` on your own Mac.
- **Check the result.** In Finder, choose Go > Go to Folder and enter `~/support-wiki-data/slim`. Open a few files and check they read as customer and agent turns, in order.
- **Full year.** When you say so, Claude runs the full download in the background. It takes a while, and you can close and re-run it: it skips tickets it already saved.
- **Never allow Claude to open `intercom-token.txt`.** If a permission prompt asks to read it, choose deny, and tell Claude not to.

## 7. When the download finishes
Claude reads `manifest.json` and reports the counts. If `possibly_truncated` is above 0, ask Claude what it means.

## 8. When you're done with the project
Delete `intercom-token.txt`, revoke the token in the Developer Hub, and delete `~/support-wiki-data` once the project no longer needs it. Don't copy the data anywhere else or attach it to email, Slack, Notion or Drive.

## If you ever prefer Terminal
Skip the token file: run `read -s "INTERCOM_TOKEN?Paste token, then press Return: "` then `export INTERCOM_TOKEN`, and run `python3 ~/support-wiki-tools/download_tickets.py --limit 20` from Terminal.
