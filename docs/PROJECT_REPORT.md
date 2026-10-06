# DataPilot AI: Engineering Project Report

Prepared 7 October 2026. Owner: AnyalstRushi. Maturity: evidence-backed portfolio prototype, not production-ready.

## 1. Executive brief
DataPilot explores a conversational interface for spreadsheet questions and email communication. The observed n8n workflow uses a chat trigger, AI Agent, Anthropic Chat Model, Simple Memory, Google Sheets retrieval, and Gmail. Screenshots show small-sheet interaction and a received static greeting email. They do not show a verified data-derived report delivered end to end.

The intended business value is fewer manual handoffs. No time saving, ROI, adoption, or company deployment has been measured or claimed.

## 2. Observed architecture
The main connection is Chat Trigger to AI Agent. The model, memory, Sheets, and Gmail attach as supporting sub-nodes. Tool invocation is agent-selected, not a guaranteed linear reporting pipeline.

One screenshot shows booking fields; another shows sales-order fields. Validate the actual schema before defining numeric metrics. Exact n8n version, model ID, granted scopes, prompts, and complete source coverage remain unconfirmed.

## 3. Evidence register
E01: Screenshot-2026-10-03-150036.jpg shows chat-agent and Sheets topology.
E02: Screenshot-2026-10-03-152132.jpg shows 20,407 returned items with booking fields.
E03: Screenshot-2026-10-03-150851.jpg shows request entity too large at the Anthropic node.
E04: Screenshot-2026-10-03-152235.jpg shows sales-order fields inside a response array.
E05: Screenshot-2026-10-03-152602.jpg shows a user asking for a row count.
E06: Screenshot-2026-10-03-152632.jpg shows a response of 43 data rows plus one header.
E07: Screenshot-2026-10-03-153906.jpg shows undefined chatInput and a Simple Memory error.
E08: Screenshot-2026-10-07-012914.jpg shows Gmail tool success, but no green Sheets execution in that same run.
E09: WhatsApp-Image-2026-10-07-at-1.24.45-AM.jpg shows receipt of a static greeting email.

These are user-supplied observations across different workflow states. Filename dates are not treated as verified execution dates. Raw screenshots are deliberately not published. The 43-row display is not an audited count of the 20,407-item source. A one-item tool output can contain an array of many rows.

## 4. Failure analysis
Sheets retrieval succeeded in the large example, but the next model request was too large. Exact payload bytes, provider limits, and service error codes were not established. Shortening the user prompt alone does not shrink raw Sheets tool output.

A separate manual agent execution lacks chat input and shows a memory error. Inspect trigger/session context and the detailed node error rather than asserting a definitive memory cause.

An empty final output does not establish whether an external email action happened. Inspect actual tool results, Sent status, and receipt before rerunning.

## 5. Proposed architecture and decisions
Validate source, schema, intended metrics, and recipient. Retrieve required data using a documented bounded strategy. Calculate counts, sums, and group-by results deterministically outside the LLM. Emit one compact summary with complete or partial coverage and quality warnings. Let the model explain that summary. Preview the exact recipient and body, require approval, send one email, and record its outcome.

Larger sources may need batch retrieval or external computation; exact implementation must be checked against the installed version. Recipient approval, prompt-injection defense, memory isolation, idempotency, and monitoring are proposed, not verified features.

Design decisions: keep arithmetic outside the model; distinguish observed and proposed functionality; separate report generation from external communication; publish no raw contacts or unreviewed exports.

## 6. Setup and reproduction
The original n8n JSON export is missing. Export the working workflow, keep a private backup, and inspect credential references, personal emails, source/workspace IDs, pinned data, sensitive prompts, and authentication headers. Add the inspected export under workflows/datapilot-agent.sanitized.json only after a clean import test.

Record n8n version, model ID, node versions, source range and filters, memory session strategy, and recipient/body mapping. Reconnect credentials locally. Import the fictional fixture into a new test sheet. Run through workflow chat so trigger input and session context exist. Verify source coverage and expected metrics, then test Gmail independently. Finally verify that the generated report body is the exact received email body.

## 7. Acceptance tests
The synthetic CSV has eight data rows and five successful bookings. Booking values total 1,000. Mean across all rows is 125; mean across successful bookings is 200. Each other status has one row. Currency is unspecified. These are fixture expectations, not original workflow measurements.

Local fixture tests check metric consistency, count, status totals, and rejection of empty, non-numeric, non-finite, or duplicate-ID inputs. They do not exercise n8n or external integrations. Hosted CI is unverified until a successful Actions run.

Workflow tests remain pending: clean import; correct source count; exact aggregates; actual dynamic-report receipt; empty source; missing-value policy; filtered source labelled partial; controlled provider errors; no false success; no duplicate sends; untrusted spreadsheet cells; and large-data retest.

Release gate: original sanitized export imports, fixture metrics match exactly, and a real data-derived report is received. Production readiness requires additional security, scale, monitoring, and recovery evidence.

## 8. Security and operations
Never publish API keys, OAuth tokens, authentication headers, raw source rows, personal contacts, private workspace URLs, pinned data, or unreviewed screenshots. The public fixture is fictional. Original dataset reuse rights are not established.

Use a fixed test recipient during development. Check actual granted scopes rather than claiming least privilege. Proposed safeguards include allowlisting, preview approval, duplicate-send ledger, minimized model input, memory boundaries, and log retention. No audit or compliance certification is claimed.

For an error, record failing node, exact message, source coverage, and prior send outcome. Do not rerun an uncertain send blindly. Do not invent missing data or claim full coverage after partial reads. If a secret is exposed, revoke or rotate it and inspect history; deleting a file alone is not sufficient.

## 9. Roadmap and interview narrative
Stage 1: original export, version record, and clean fixture reproduction.
Stage 2: deterministic aggregation, coverage validation, and dynamic report email.
Stage 3: exact-content approval and duplicate prevention.
Stage 4: bounded large-source retrieval and compact model input.
Stage 5: explicit error paths, retention, monitoring, and recovery tests.

Demo: explain the problem; show architecture; explain the small-sheet result; show static email receipt without calling it an analytics report; show the large-payload failure; discuss the proposed aggregation-first redesign.

Resume wording: Built an n8n conversational spreadsheet and Gmail automation prototype using an Anthropic model and session memory; demonstrated small-sheet interaction and email delivery, and documented a large-payload failure with an aggregation-first redesign proposal.

## 10. Official technical sources
n8n export/import: https://docs.n8n.io/build/manage-workflows/export-and-import
n8n Sheets operations: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations
n8n Tools Agent: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
n8n Gmail operations: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations
GitHub upload guidance: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

These support platform guidance, not unobserved project outcomes. Inspect installed-version documentation and the original export before implementation claims.
