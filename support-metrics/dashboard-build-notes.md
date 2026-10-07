# Dashboard build notes (NOT for the wiki)

These notes name individuals and cover build decisions. Individual figures live on the dashboard only, visible to Shanise only for now.

## Teammate IDs (Intercom admin IDs)
- Jose: 7853193
- Veronica: 9954357
- Support team ID: 7086066
- Individual panels show Jose and Veronica only. Team metrics include every assignee and unassigned tickets.

## Decisions made (2026-10-07)
- Fin-only and Fin-resolved tickets are excluded. Fin-escalated tickets answered by a human count.
- Business hours: Mon-Fri 9:00-18:00 America/New_York (DST-aware), 9 holidays (see wiki definitions). SLA of "1 business day" means 9 business hours.
- Closed tickets are credited to the assignee; unassigned counts toward team only.
- Reopen rate uses Intercom's raw reopen count.
- Open tickets include unassigned and teammates other than Jose and Veronica.

## Build-time checks still open
1. Confirm Intercom's "first teammate reply" stat never counts a Fin reply. Check against real tickets before trusting first-response numbers.
2. Holidays that fall on a weekend: default is the federal observance (Saturday observed Friday, Sunday observed Monday). Confirm with Shanise.
3. Some closed tickets have no assignee but were closed by Jose. Under the approved rule these count toward team only, so Jose's weekly closed count will read lower than his closes.
4. The 9/18 baselines are probably plain clock time and cover Jose and Veronica only. Re-run them on these definitions before comparing to goals.
5. Open tickets history cannot be rebuilt from Intercom, so the trend starts when daily snapshots begin.
6. Confirm whether "unassigned" includes tickets with no team at all, not just no teammate.

## Data source plan
1. BigQuery first (to be confirmed once repo access arrives). Aggregates by SQL, no ticket text leaves the warehouse.
2. Fallback: a local script on Shanise's Mac that writes only totals and medians.
3. Connector use limited to small counts such as open tickets. Responses include full message bodies with customer details, so avoid it for bulk pulls.
4. The dashboard stores aggregates only, never ticket text or customer details.

## Order of work
1. Re-run baselines on the approved definitions and compare to the 9/18 numbers.
2. Build the data layer and daily open-ticket snapshot.
3. Build the dashboard: team tiles against goals, per-teammate panels, weekly trend, last-refreshed stamp.
4. Move the definitions into the wiki's metrics section and link the dashboard.
