# Kirill

I build tools that people can run and inspect themselves. My recent work covers document review, data comparison, webhook debugging, and file analysis, using Python, TypeScript, C#, and Java.

## Selected work

### Student AI Checker

A local app for teachers reviewing DOCX coursework. It extracts text and images, asks a local Ollama model to assess approved criteria, then validates scores and evidence references in Python. Teachers can review uncertain results in the web interface or desktop app.

The [synthetic demo](https://github.com/musyase/student-ai-checker#english-overview) runs without Ollama. [Unit tests](https://github.com/musyase/student-ai-checker/actions/workflows/unit-tests.yml) run on Windows and Ubuntu. Grading quality still needs an independent study with teacher-scored work.

[Repository](https://github.com/musyase/student-ai-checker) | [Evaluation plan](https://github.com/musyase/student-ai-checker/blob/main/docs/quality-evaluation.md)

### CSV Change Review

A browser tool for comparing two CSV exports by a shared record key. It shows changed fields, added and removed records, and schema changes. Files stay in the browser. The demo opens with fictional data and can be replaced with local CSV files.

[Live demo](https://musyase.github.io/csv-change-review/) | [Repository](https://github.com/musyase/csv-change-review) | [Tests](https://github.com/musyase/csv-change-review/actions/workflows/ci.yml)

### Webhook Desk

A local ASP.NET Core inbox for reproducing webhook failures. It stores UTF-8 events in SQLite, deduplicates deliveries with an event ID, and replays the original bytes to a loopback HTTP target. Each replay records its status or connection error.

[Repository and local walkthrough](https://github.com/musyase/webhook-desk) | [Tests](https://github.com/musyase/webhook-desk/actions/workflows/tests.yml)

## Other work

- [folder-audit](https://github.com/musyase/folder-audit): finds duplicate files, compares folder snapshots by content, and identifies unambiguous file moves. The [HTML sample report](https://musyase.github.io/folder-audit/demo.html) opens offline.
- [Site Change Ledger](https://github.com/musyase/site-change-ledger): checks selected text on a web page, uses ETag when available, and keeps a SQLite history with diffs. Its demo runs against a temporary local server.
- [Stav Electroset](https://github.com/musyase/stav-electroset-app): an Android news reader prototype in Java, with Room storage and a WordPress API fallback.
- [FRVehicleDamageControl](https://github.com/musyase/FRVehicleDamageControl): a C# game plugin for changing vehicle damage settings.
