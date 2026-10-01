# Claim status check SOP

Draft v1, written 2026-10-01 for the support team. This is a private working page. It moves to the support wiki once Shanise and Jack have reviewed it, and the wiki page then becomes the one to edit.

## Purpose
Customers ask where their claims stand: whether a session was paid, denied, rejected or applied to the deductible. Support takes the first pass. Support checks the status (the Admin UI, then the Change API button, then Availity), replies to the customer with the status of each claim, and hands off to billing only when the claim needs action. Billing then resolves it: resubmitting, registering a provider, or following up with the insurer.

Whoever is assigned the ticket owns both the reply and the close.

> Timing. First response within 1 business day, with a target median under 6 hours. Resolution in 3 to 5 business days, with a goal of cutting that in half. Update the customer every 2 days with something substantive.

## Step 1. Is it a claim status request?
- **Claim status request:** the customer asks where a claim stands, whether a session was paid, or why a claim was denied or applied to the deductible. Continue to step 2.
- **An insurer is asking for medical records:** use SOP 3, not this one.
- **Payment sent but the customer never got it:** hand off to billing (step 5). Billing checks with the insurer for payment details and, if needed, requests the payment be reissued.
- **Claims submitted less than 30 days ago, with no sign of a denial or rejection:** do not run a status check. Reply with the "still processing" template in step 3.
- **Not sure:** treat it as a claim status request and continue.

## Step 2. Check the status
1. In the Admin UI, find the client and press the Change API button. See if the claims update.
2. If the status is still unclear, log into Availity and look up the claims. Availity is the only portal support has access to for now. This SOP will be updated as access to other portals is given. Superdial is not part of the current process.
3. Write down the status for each date of service: paid, deductible, rejected or denied, and the reason for any rejection or denial. Never write exact payment amounts.
4. If you have checked all of the above and still can't get a status, hand it off to billing (step 5).

## Step 3. Reply to the customer
- Give one line per date of service with the status and the reason. Never quote exact payment amounts. The right level of detail: "DOS 8/17 denied due to timely filing, the rest are paid."
- Tell the customer they can check claim statuses themselves in the Sessions + Claims tab of their Mentaya account.
- Say what happens next and when. Never just "we're looking into it."
- Follow the support style guide: concise, solutions first, no apologies, and a concrete next step. Sign off with your name and @ Mentaya.

Templates are drafts for Shanise to approve. Fill in the bracketed parts and never invent a fact you don't have.

**If every claim is paid**
```text
Hi [First name],

Quick update on the claims for [client initials]: [dates of service] are all paid. Nothing more is needed from you.

You can check claim statuses anytime in the Sessions + Claims tab of your Mentaya account.

[Your name] @ Mentaya
```

**If a claim was applied to the deductible**
```text
Hi [First name],

Quick update on the claims for [client initials]: [date of service] was applied to the deductible. That means [payer] counted the payment toward the amount the plan requires before it starts paying. [Other dates] are paid.

No action is needed from you. You can check statuses anytime in the Sessions + Claims tab of your Mentaya account.

[Your name] @ Mentaya
```

**If a claim was denied or rejected and billing is fixing it**
```text
Hi [First name],

Update on the claims for [client initials]: [date of service] was [denied / rejected] by [payer] because [reason]. Our billing team is [correcting and resubmitting it / handling the next steps], and you can expect an update within [3 to 5 business days].

[Other dates] are paid. You can check statuses anytime in the Sessions + Claims tab of your Mentaya account.

[Your name] @ Mentaya
```

**If we need something from the customer first**
```text
Hi [First name],

Update on the claims for [client initials]: [date of service] was [rejected / denied] because [reason]. To resubmit it, [payer] needs [item, such as a W-9].

[For a W-9: You can upload your W-9 in Settings in your Mentaya account and we'll send it to the payer.] Once we have it, our billing team resubmits the claim and we'll confirm when it's done.

[Your name] @ Mentaya
```

**If the claim is still processing (under 30 days)**
```text
Hi [First name],

Quick update on the claim for [session date]: it's still moving through [payer]'s review. This is normal. Out-of-network claims like this typically take [X weeks] to process, and yours is on track.

No action needed on your end. We're keeping an eye on it and will follow up the moment there's movement.

[Your name] @ Mentaya
```

**If you couldn't get a status and billing is checking**
```text
Hi [First name],

Update on the claims for [client initials]: we checked [payer]'s system and don't yet see a status for [date of service]. Our billing team is following up with [payer] directly, and you can expect an update within [3 to 5 business days].

[Your name] @ Mentaya
```

## Step 4. Handle it or hand it off
**Handle it yourself (reply only) when:**
- Every claim is paid.
- A claim was applied to the deductible.
- The claim is still processing and was submitted less than 30 days ago.
- You found the status and no action is needed.

**Hand off to billing when:**
- The claim needs action: it must be resubmitted because it was denied or rejected, or the provider needs to be registered.
- You couldn't get a status after checking the Admin UI, the Change API and Availity.
- The payment was sent but the customer never received it.

**If resubmitting needs more information** (a W-9, medical records), support contacts the provider or client first to get it, then hands off to billing to resubmit. For a W-9, the provider uploads it in Settings in their Mentaya account and Mentaya sends it to the payer. For medical records, use SOP 3.

## Step 5. Hand off to billing
1. In the Admin UI, open the Patient tab, then Patient, then Account Health Check +, with a delay of 0 days. If an Account Health Check (AHC) already exists, use it. There is only one AHC type.
2. Fill in the note's four fields, using this format:
   ```text
   SOURCE: [Admin UI / Change API / Availity]
   STATUS: [paid / deductible / rejected / denied, per date of service. No exact amounts.]
   CONTEXT: [the rejection or denial reason]
   ACTIONS TAKEN: [what you did, and where]
   Flag: [6+ months old / high-priority or high-revenue practice / none]
   ```
3. Link the AHC to its Linear issue in the billing project (BIL) and to the Intercom ticket. Label it "Support Request."
4. Priority is Medium. Flag it in Linear if the claim is 6 or more months old, or if the practice is high priority or high revenue.
5. Tell the customer what happens next, using the matching template in step 3.

## Step 6. Follow up and close
- **Waiting on documents from the customer:** follow up 3 times, once a week. After 3 attempts, tell billing they can cancel their task. The Intercom ticket can then be closed.
- **Close** only with a clear resolution: most claims are progressing, you shared what you found, or you followed up and heard nothing. Don't close while claims are still denied, the provider is still upset, or other claims are still waiting.
- **Snooze** when waiting on a provider, when you promised to check back in 2 to 3 weeks, or when waiting on engineering or billing. Don't snooze if the provider replied with a question.
- A linked Linear issue moved to Waiting reopens the Intercom conversation.

## Worked example (invented for illustration)
The names, dates and payer are made up.

A provider writes: "Can you tell me where the claims for my client AB stand? Sessions on 9/2, 9/9 and 9/16."

1. In the Admin UI, support presses the Change API button. The 9/9 and 9/16 claims update to paid. The 9/2 claim doesn't change.
2. In Availity, the 9/2 claim shows as rejected for a missing tax ID.
3. Resubmitting needs a W-9, so support asks the provider first (step 4) and replies:
   ```text
   Hi [First name],

   Update on the claims for AB: 9/9 and 9/16 are paid. 9/2 was rejected because the payer needs your tax ID. To resubmit it, upload your W-9 in Settings in your Mentaya account and we'll send it to the payer. Once we have it, our billing team resubmits the claim and we'll confirm when it's done.

   You can also check claim statuses anytime in the Sessions + Claims tab of your Mentaya account.

   [Your name] @ Mentaya
   ```
4. The provider uploads the W-9. Support opens the AHC and hands off:
   ```text
   SOURCE: Admin UI, Change API, Availity
   STATUS: 9/2 rejected; 9/9 and 9/16 paid
   CONTEXT: 9/2 rejected for a missing tax ID; the provider uploaded a W-9
   ACTIONS TAKEN: Checked the Change API and Availity; asked the provider for a W-9; the provider uploaded it
   Flag: none
   ```

## Open items before this moves to the wiki
- The reply templates are drafts and need Shanise's approval.
- "Flag it in Linear" doesn't yet say how: a priority change, a label, or a comment.
- The processing time for the still-processing template ("[X weeks]") is not set.
- The reply for claims under 30 days (step 1) is assumed from the 30-day rule. Confirm it.
- Add steps for other portals as access is given.
- Link SOP 3 and the wiki once the wiki's home is decided.

## Where the facts come from
- Support Wiki v1: Shanise's Working Version (SOP 6 and the confirmed steps)
- Success metrics (response and resolution targets)
- Support style guide (reply format)
