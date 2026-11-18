# Kirill

I build tools for document review, data comparison, field auditing, and debugging. These projects show work in Python, Kotlin, TypeScript, C#, and Java. Each featured repository has a way to try it and a specific part of the code to inspect.

## Featured projects

### [Student AI Checker](https://github.com/musyase/student-ai-checker)

A local DOCX review app for teachers. It extracts text and images, asks Ollama to assess approved criteria, and checks scores and evidence IDs in Python. The teacher can resolve uncertain cases in a web or desktop interface.

The [fictional demo](https://github.com/musyase/student-ai-checker#try-the-review-workflow) runs without Ollama. The interface is currently in Russian. Grading accuracy still needs a study with teacher-scored work.

Inspect the [validator](https://github.com/musyase/student-ai-checker/blob/main/src/student_ai_checker/grading/validator.py), [teacher review code](https://github.com/musyase/student-ai-checker/blob/main/src/student_ai_checker/teacher_review.py), and [tests](https://github.com/musyase/student-ai-checker/actions/workflows/unit-tests.yml).

### [Pocket Audit](https://github.com/musyase/pocket-audit)

An offline Android app for checking equipment against a CSV inventory. It scans labels on the device, records condition and optional photos, then exports a ZIP report. Unchecked items become missing only when the audit is completed. The ZIP includes checksums that an independent Python script can verify.

The app starts with fictional workshop data. Download the [debug APK](https://github.com/musyase/pocket-audit/releases/download/v0.1.0/pocket-audit-debug.apk) or see the [emulator screenshots](https://github.com/musyase/pocket-audit#screenshots). Inspect the [CSV parser](https://github.com/musyase/pocket-audit/blob/main/app/src/main/java/dev/musyase/pocketaudit/domain/InventoryCsv.kt), [audit rules](https://github.com/musyase/pocket-audit/blob/main/app/src/main/java/dev/musyase/pocketaudit/domain/AuditLogic.kt), and [Android checks](https://github.com/musyase/pocket-audit/actions/workflows/android.yml).

### [CSV Change Review](https://github.com/musyase/csv-change-review)

A browser tool for comparing CSV exports by a shared key. It shows field changes, added and removed records, and schema drift. Files are read in the browser and are not uploaded.

Try the [live sample](https://musyase.github.io/csv-change-review/) with fictional data, then inspect the [comparison logic](https://github.com/musyase/csv-change-review/blob/main/src/compare.ts) and [tests](https://github.com/musyase/csv-change-review/blob/main/src/compare.test.ts).

### [Webhook Desk](https://github.com/musyase/webhook-desk)

A local ASP.NET Core inbox for reproducing webhook failures. It stores events in SQLite, deduplicates deliveries by event ID, and replays the original bytes to a loopback target. Replay outcomes are recorded.

The README has a local walkthrough. Inspect the [event store](https://github.com/musyase/webhook-desk/blob/main/src/WebhookDesk/EventStore.cs) and [HTTP tests](https://github.com/musyase/webhook-desk/blob/main/tests/WebhookDesk.Tests/ApiTests.cs).

### [folder-audit](https://github.com/musyase/folder-audit)

A Python CLI for finding duplicate files and comparing folder snapshots by content. It identifies a move only when the matching hash is unambiguous and can generate a single HTML report that opens offline.

Open the [sample report](https://musyase.github.io/folder-audit/demo.html), then inspect the [core logic](https://github.com/musyase/folder-audit/blob/main/src/folder_audit/core.py) and [tests](https://github.com/musyase/folder-audit/blob/main/tests/test_core.py).

## Also built

- [Site Change Ledger](https://github.com/musyase/site-change-ledger): a Python CLI that checks selected text on a web page and keeps a SQLite history. Its demo runs against a temporary local server.
- [Stav Electroset](https://github.com/musyase/stav-electroset-app): a Java Android news reader prototype with Room storage and a WordPress API fallback. It builds in CI; automated UI tests are still missing.
