# Instructions for my local Claude session (paste as the first message)

I'm Shanise, on the Mentaya support team. We're building a support wiki: validated answers to customer questions, plus SOPs. The plan and design decisions are in the Playbook doc: https://claude.ai/artifact/RbXFh9kRJL8YgqM3Yh9hCh (tabs: Playbook, Wiki v1 draft, Notion cleanup list). Read the Playbook tab first and play back what we're building before doing anything. Don't build anything yet.

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
