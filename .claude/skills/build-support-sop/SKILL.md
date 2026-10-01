---
name: build-support-sop
description: Build Mentaya support SOPs in the team's house style (the format of Jack's partnership inquiry SOP). Use whenever Shanise or anyone on support asks to build, draft, write, update or convert an SOP, process doc or "how we handle X" page, including claim status, escalation, refund, onboarding and bug-report SOPs, even if they don't say "template" or "format". Gathers context from the support wiki and Notion first, then asks only the questions that need Shanise's direct input before building.
---

# Build a Mentaya support SOP

The goal: when someone asks for an SOP, the format, style and Mentaya context are already in hand. Build from what is already known, and ask only about what is missing.

## Workflow

1. **Gather before asking.** Read, in this order:
   - `references/mentaya-context.md` (people, systems, targets, channels, macros, existing SOPs). It is a dated snapshot, so check anything that matters against the wiki.
   - The support wiki working version (link in the context file) for confirmed steps, decisions and rules. Facts there ticked by Shanise are confirmed.
   - Related Notion pages, Linear, Slack and Intercom through the connectors, as leads only. Never treat an old ticket reply, an archived page or a Slack thread as a fact.
2. **Fill the intake checklist below** from those sources. Mark each item: **answered** (a confirmed source states it), **partly answered** (a general rule exists but nothing specific to this SOP), or **missing** (nothing). If the wiki or Notion can't be read, say so in the flag message and treat everything as unconfirmed.
3. **Flag, don't guess.** If anything is missing or in conflict, send one numbered message before building and wait for her reply. See "What to flag". If nothing is missing, build without asking. Once she replies, use her answers, use the defaults for anything she says "yes" to, and put anything she can't answer into the page's "Open items". Then build.
4. **Build** the SOP in the house style below. Create it as a **private Notion draft** (`creation_mode: "draft"`) unless Shanise names a destination. Use `references/sop-template.md` as the skeleton and `references/example-claim-status-sop.md` as the finished example.
5. **Report in a few lines:** the page link, that it is private, the open items list from the page, and any assumptions. Never move it into the wiki or share it unless asked.

## Intake checklist

| # | Input | Usually found in |
| --- | --- | --- |
| 1 | Trigger and scope: what arrives, from whom, and what is out of scope | wiki, Intercom patterns |
| 2 | Who does it, and who decides | context file, wiki |
| 3 | The steps in order, with the exact system, screen or button | wiki, existing Notion pages |
| 4 | Access and prerequisites (which tools support can actually use) | context file, Shanise |
| 5 | Decision points: handle it, hand it off, or escalate, with the criteria | wiki |
| 6 | Escalation path: who, where, when, and what to include | context file |
| 7 | Timing: first response, resolution, update and follow-up cadence | context file (Success metrics) |
| 8 | Priority rules and what raises them | context file |
| 9 | Customer replies needed, one per outcome | style guide skill, Shanise to approve |
| 10 | Exceptions and who approves them | wiki, Shanise |
| 11 | A worked example | invent one, no patient details |
| 12 | Validation status: which steps Shanise has confirmed | wiki ticks |

## What to flag

Ask Shanise only when one of these is true:
- No confirmed source answers the checklist item.
- Two sources disagree and no decision is recorded.
- It needs her approval, such as reply template wording or an exception rule.

Do not ask about anything the context file or the wiki already answers, or anything she already decided. Send **one message**, numbered, and for each question say what you found and what you would default to, so she can reply "yes". Keep the SOP unbuilt until she answers.

## House style

This follows Jack's partnership inquiry SOP. The structure, in order:

1. **Draft line.** "Draft v1, written [date] for [audience]. This is a private working page. It moves to the support wiki once [reviewers] have reviewed it, and the wiki page then becomes the one to edit."
2. **Purpose.** Two to four sentences: what arrives, who does what, and who decides. Add the bar for stopping or escalating if there is one.
3. **Timing callout** when targets apply.
4. **Numbered steps**, headed "Step N. [Question or action]". Step 1 is almost always "Is it X?" with the not-X cases and where they go. Last step covers follow-up and closing.
5. **Decision criteria** as short bullet lists: "Handle it yourself when" and "Hand off or escalate when". Include an "Always bring it to [person], even if you lean no" list where it applies.
6. **Post or handoff format** as a code block with labeled fields.
7. **Reply templates**, one per outcome, each in a code block, labeled by when to use it.
8. **Worked example**, invented, with the note that names, dates and payer are made up.
9. **Open items before this moves to the wiki.** Everything unconfirmed or assumed.
10. **Where the facts come from.** Links, not copies.

Voice: plain words, short sentences, imperative. Say who does the step. Say "support", not "the agent". Use numbers and names, never "soon" or "appropriate". No filler openers and no apologies in customer replies.

## Rules

- **Source ranking:** product code, then product docs, then Shanise. Current Notion pages are leads until she confirms. Never use old tickets, archived pages, old help articles or Slack threads as facts.
- **One home per fact.** Targets, SLAs, prices and fees live in one place. Link to them and don't restate them, unless the SOP step can't work without the number. Then repeat it and link its home.
- **Customer replies** follow the support style guide (the `draft-support-response` skill holds it). Placeholders in square brackets, never an invented fact, no exact payment amounts, sign off with name and @ Mentaya.
- **Escalation pattern:** post in a public channel, not a DM, tag the decider, link the Intercom conversation, and use a fixed field format. The support meeting notes are a fallback for anything stuck more than a day, in addition to the post, not instead of it.
- **Priority:** the defaults in the context file are general. If the SOP sets its own priority (for example, claim status checks are Medium), state it explicitly in the SOP and let it win.
- **No patient or client details** in the SOP, the example or the templates. Initials only where a reply needs a client reference.
- **Mark the unconfirmed.** Anything not ticked by Shanise goes in "Open items" or is labeled as an assumption.

## Notion formatting gotchas

- Set the title in properties, not at the top of the content.
- Outside code blocks, escape square brackets and other special characters. Put templates and field formats in code blocks to avoid escaping.
- A code block between numbered steps restarts the numbering. Indent it with a tab under its step to keep the count.
- Use a date mention for dates and a callout for the timing note.
- After a structural edit, fetch the page again and check it.
