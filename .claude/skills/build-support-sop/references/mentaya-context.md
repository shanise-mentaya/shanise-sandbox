# Mentaya support context (snapshot, 2026-10-01)

This is a snapshot, not a source of truth. The support wiki working version holds the confirmed facts. If something here matters to the SOP, check it there first, and update this file when it has changed.

## Where the confirmed facts live
- Support wiki working version (Shanise's doc): https://claude.ai/artifact/64J26LuXtfSh2eGqGCiNak
  - Tab 1 holds the decisions, the ticket pilot and the claim status SOP.
  - Tab 2, "Wiki draft (v1)", holds Part 1 (customer questions) and Part 2 (SOPs 1 to 6). A tick means Shanise confirmed it.
- Jack's original handoff Playbook: https://claude.ai/artifact/RbXFh9kRJL8YgqM3Yh9hCh
- Reply style guide: https://app.notion.com/p/3d1ed73d7cc980788dc7ef6b086f6a45 (the `draft-support-response` skill summarizes it)
- Success metrics: https://app.notion.com/p/3cfed73d7cc98186b1bfe1a08a9b2df4
- Finished example SOP: `example-claim-status-sop.md` in this folder (private Notion draft: https://app.notion.com/p/3eced73d7cc981bb9f66df14995e03bc)

## People and roles
- **Shanise** owns the support SOPs and the wiki working version. She manages Jose and Veronica, who work the support inbox.
- **Jack** sponsors the wiki project and decides on partnership inquiries. His partnership inquiry SOP is the model for the house style.
- **Jincy** is building a similar project for billing. Keep the SOP structure compatible with it.
- **Billing** resolves claim problems that support hands off: resubmitting, registering providers, calling insurers.
- **Leadership** approves exceptions, such as lifting a Premera block for a practice.

## Systems
- **Intercom:** the support inbox, macros and the help center (help.mentaya.com). Macros are mostly unused and outdated, and a macro audit is planned. Link macros by name only if Shanise confirms they are current.
- **Admin UI:** patient records, claims, the Change API button (support presses it to see if claims update), and Account Health Checks (AHCs).
- **Account Health Check (AHC):** an Admin UI record plus a linked Linear issue in the billing project, BIL. Create it from Patient tab, Patient, Account Health Check +, delay of 0 days. There is only one AHC type. Label it "Support Request". Note fields: SOURCE, STATUS, CONTEXT, ACTIONS TAKEN.
- **Linear:** billers work from Linear. Flag priority there.
- **Availity:** the only insurance portal support can use for now. Other portals will be added as access is given.
- **Superdial:** not part of the current process, though it may return.
- **Slack:** work in public channels by default. #support for support work, #on-call for urgent issues.

## Targets (home: Success metrics, Notion, 9/18)
- First response SLA: within 1 business day. Target: median under 6 hours per agent, with 4 hours as the ultimate goal.
- Backlog goal: under 15 open tickets at end of day, excluding snoozed.
- Resolution: 3 to 5 business days, with a goal of cutting that in half. Update the customer every 2 days with something substantive.

## Priority (home: SOP 1 in the wiki)
- **High:** angry customers, anything money-related, anything blocking claim submission, claim issues, bugs, starred customers.
- **Medium:** claim status checks, high-intent customers with unusual asks.
- **Low:** eligibility requests, feature requests that do not block submission.
- Within a priority, rank by revenue impact.

## Escalation rules that already exist
- Work in passes: answers under 5 minutes first, then up to 10 minutes of investigation, then hand anything over 10 to 15 minutes to the owner or on-call.
- Escalate anything stuck more than a day into the support meeting notes.
- One conversation, one owner. The assigned person owns both the reply and the close.
- If three customers ask the same thing in a week, flag it in Slack and push for a help article or process change.
- Partnership offers: post in #support, tag Jack and Shanise, and support sends the reply after Jack decides.

## Existing SOPs (wiki tab 2)
SOP 1 daily inbox triage, SOP 2 opening an Account Health Check, SOP 3 medical-records request, SOP 4 refunds and voids, SOP 5 manual eligibility check (billing's SOP, kept for reference), SOP 6 claim status check. Jack's partnership inquiry SOP lives outside the wiki.

## SOP backlog: escalation-related, in suggested order
1. Bug escalation to engineering (no source yet)
2. Urgent or on-call escalation (partial)
3. At-risk or angry provider (partial)
4. Payer-level escalation, such as Premera and Anthem (partial)
5. Leadership exception approval (partial)
6. Recurring-issue flagging (one line in the principles)
7. Feature request intake (none exists)
8. Billing handoff, SOP 2 (partial)

## Terms
OON: out-of-network. AHC: Account Health Check. DOS: date of service. BIL: the billing project in Linear. SOP 3 is the medical-records SOP.

## Handling data
Tickets contain patient information and stay on Shanise's Mac. SOPs, templates and examples must never contain patient or client names, dates of birth, member IDs, emails or phone numbers. Invent worked examples.
