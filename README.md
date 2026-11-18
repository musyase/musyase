# Kirill

I build tools for document review, field audits, data comparison, scheduling, and debugging. The featured projects use Python, Kotlin, Flutter/Dart, TypeScript, Go, and C#. Each repository has a way to try it and a specific part of the code to inspect.

## Featured projects

### [Student AI Checker](https://github.com/musyase/student-ai-checker)

A local DOCX review app for teachers. It extracts text and images, asks Ollama to assess approved criteria, and checks scores and evidence IDs in Python. The teacher can resolve uncertain cases in a web or desktop interface.

The [fictional demo](https://github.com/musyase/student-ai-checker#try-the-review-workflow) runs without Ollama. The interface is currently in Russian. Grading accuracy still needs a study with teacher-scored work.

Inspect the [validator](https://github.com/musyase/student-ai-checker/blob/main/src/student_ai_checker/grading/validator.py), [teacher review code](https://github.com/musyase/student-ai-checker/blob/main/src/student_ai_checker/teacher_review.py), and [tests](https://github.com/musyase/student-ai-checker/actions/workflows/unit-tests.yml).

### [Pocket Audit](https://github.com/musyase/pocket-audit)

An offline Android app for checking equipment against a CSV inventory. It scans labels on the device, records condition and optional photos, then exports a ZIP report. Unchecked items become missing only when the audit is completed. The ZIP includes checksums that an independent Python script can verify.

The app starts with fictional workshop data. Download the [debug APK](https://github.com/musyase/pocket-audit/releases/download/v0.1.0/pocket-audit-debug.apk) or see the [emulator screenshots](https://github.com/musyase/pocket-audit#screenshots). Inspect the [CSV parser](https://github.com/musyase/pocket-audit/blob/main/app/src/main/java/dev/musyase/pocketaudit/domain/InventoryCsv.kt), [audit rules](https://github.com/musyase/pocket-audit/blob/main/app/src/main/java/dev/musyase/pocketaudit/domain/AuditLogic.kt), and [Android checks](https://github.com/musyase/pocket-audit/actions/workflows/android.yml).

### [Meeting Window](https://github.com/musyase/meeting-window)

A Flutter app that finds shared meeting times from each person's local working hours. It handles daylight saving gaps and repeated hours, shows local UTC offsets, and exports an `.ics` invitation. People and hours are saved on the device.

Try the [web app](https://musyase.github.io/meeting-window/) or download the [Android demo](https://github.com/musyase/meeting-window/releases/download/v0.1.0/meeting-window-android-demo.apk). Inspect the [time calculation](https://github.com/musyase/meeting-window/blob/main/lib/window_finder.dart), [clock change tests](https://github.com/musyase/meeting-window/blob/main/test/window_finder_test.dart), and [build checks](https://github.com/musyase/meeting-window/actions/workflows/check.yml).

### [CSV Change Review](https://github.com/musyase/csv-change-review)

A browser tool for comparing CSV exports by a shared key. It shows field changes, added and removed records, and schema drift. Files are read in the browser and are not uploaded.

Try the [live sample](https://musyase.github.io/csv-change-review/) with fictional data, then inspect the [comparison logic](https://github.com/musyase/csv-change-review/blob/main/src/compare.ts) and [tests](https://github.com/musyase/csv-change-review/blob/main/src/compare.test.ts).

### [Trace Weave](https://github.com/musyase/trace-weave)

A Go CLI that reconstructs interleaved JSONL spans into request timelines. It points out slow calls, error spans, missing parents, cycles, and inconsistent timing. The generated report is one HTML file that opens without a server.

Open the [sample report](https://musyase.github.io/trace-weave/demo.html), then inspect the [trace analysis](https://github.com/musyase/trace-weave/blob/main/internal/trace/trace.go), [HTML renderer](https://github.com/musyase/trace-weave/blob/main/internal/render/html.go), and [tests](https://github.com/musyase/trace-weave/tree/main/internal).

### [Webhook Desk](https://github.com/musyase/webhook-desk)

A local ASP.NET Core inbox for reproducing webhook failures. It stores events in SQLite, deduplicates deliveries by event ID, and replays the original bytes to a loopback target. Replay outcomes are recorded.

The README has a local walkthrough. Inspect the [event store](https://github.com/musyase/webhook-desk/blob/main/src/WebhookDesk/EventStore.cs) and [HTTP tests](https://github.com/musyase/webhook-desk/blob/main/tests/WebhookDesk.Tests/ApiTests.cs).

## Also built

- [Folder Audit](https://github.com/musyase/folder-audit): a Python CLI for finding duplicate files and comparing folder snapshots by content. Its [sample HTML report](https://musyase.github.io/folder-audit/demo.html) opens offline.
- [Site Change Ledger](https://github.com/musyase/site-change-ledger): a Python CLI that checks selected text on a web page and keeps a SQLite history. Its demo runs against a temporary local server.
- [Stav Electroset](https://github.com/musyase/stav-electroset-app): a Java Android news reader prototype with Room storage and a WordPress API fallback. It builds in CI; automated UI tests are still missing.
