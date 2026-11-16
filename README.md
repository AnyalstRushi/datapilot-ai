<div align="center">

<img src="assets/datapilot-hero.svg" alt="DataPilot AI — Ask. Analyze. Deliver." width="100%">

# DataPilot AI

### Ask your spreadsheet. Understand the answer. Deliver with confidence.

An evidence-backed **n8n prototype** connecting conversational chat, an Anthropic Chat Model, Google Sheets, Simple Memory, and Gmail.

[![Status](https://img.shields.io/badge/status-prototype-fbbf24)](docs/PROJECT_REPORT.md)
[![Platform](https://img.shields.io/badge/platform-n8n-EA4B71?logo=n8n&logoColor=white)](https://n8n.io/)
[![Model](https://img.shields.io/badge/model-Anthropic-191919?logo=anthropic&logoColor=white)](https://www.anthropic.com/)
[![Data](https://img.shields.io/badge/data-Google%20Sheets-34A853?logo=googlesheets&logoColor=white)](https://sheets.google.com/)
[![Delivery](https://img.shields.io/badge/delivery-Gmail-EA4335?logo=gmail&logoColor=white)](https://mail.google.com/)

[![🎬 Launch interactive presentation](https://img.shields.io/badge/🎬-Launch%20interactive%20presentation-38bdf8)](presentation/datapilot-ai-presentation.html)
[![📄 Project report](https://img.shields.io/badge/📄-Project%20report-a78bfa)](docs/PROJECT_REPORT.md)

</div>

> [!IMPORTANT]  
> **Status: prototype.** Small-sheet interaction and delivery of a static email are demonstrated in supplied screenshots. Large raw-row model input failed. An end-to-end data-derived report and the original sanitized workflow export are still pending.

## Live architecture

<img src="assets/datapilot-architecture.svg" alt="DataPilot AI animated architecture" width="100%">

```text
Ask → Retrieve spreadsheet context → Reason with AI → Deliver by email
```

Connected tools do not necessarily execute on every request.

## Live demo

<img src="assets/datapilot-demo.svg" alt="DataPilot AI live demo terminal" width="100%">

```bash
python -m pip install -r requirements.txt
python scripts/validate_fixture.py
python -m unittest discover -s tests -v
python scripts/build_deliverables.py
```

The included eight-row fixture is fictional. Fixture tests validate calculations and invalid inputs only; they do not run n8n, Anthropic, Google Sheets, or Gmail.

## Evidence board

| Capability | Evidence and boundary |
|---|---|
| Spreadsheet retrieval | ✅ Sheets output shows successful retrieval |
| Small-sheet response | ✅ One agent result displays 43 data rows plus a header |
| Email delivery | ⚠️ A received email contains a static greeting, not an analytics report |
| Large-data processing | ❌ 20,407 returned items followed by `request entity too large` |
| Dynamic analytics email | ⏳ Not yet verified |
| Reproducible workflow import | ⏳ Blocked until the original workflow JSON is provided |

## Target redesign

```text
Google Sheets → External aggregation → Compact validated summary
              → Anthropic explanation → Approval → Gmail delivery
```

The target redesign calculates counts and aggregates outside the model, sends a compact validated summary for explanation, and adds an approval step before the email action.

## Interactive presentation

[![Open presentation](https://img.shields.io/badge/🎬-Launch%20presentation-38bdf8)](presentation/datapilot-ai-presentation.html)

## Start here

- [Project report](docs/PROJECT_REPORT.md)
- [Workflow export requirements](workflows/README.md)
- [Presentation content](presentation/slides.json)
- [Interactive presentation](presentation/datapilot-ai-presentation.html)

## Tests and maturity

No customer adoption, ROI, accuracy percentage, SLA, deployment claim, or security certification is made.

Original screenshots and raw source data are excluded because they contain personal contacts, private workspace details, or source records. Evidence observations are recorded in the report; images are not public in this repository.

## Roadmap

- [ ] Provide and import the original sanitized workflow JSON
- [ ] Verify end-to-end data-derived email delivery
- [ ] Implement external aggregation for large datasets
- [ ] Add a controlled approval flow for email actions
- [ ] Expand validation beyond the eight-row fixture

## Project owner

Built by [AnyalstRushi](https://github.com/AnyalstRushi) · Documentation prepared 7 October 2026

No reuse license has been selected; third-party software retains its own terms.

---

<div align="center">

**ASK. ANALYZE. DELIVER.**

⭐ If DataPilot AI helps you think about AI automation and spreadsheet workflows, star the repository.

</div>