# Kirill

I build software that runs on the user's computer. Recent projects include a DOCX review app for teachers and a file inventory tool.

## Selected work

### Student AI Checker

A teacher can load a folder of DOCX submissions, review scores against the original text, and resolve cases that need a human decision. The app runs locally with Ollama. Its Python code extracts evidence from documents and checks model output against approved criteria. It also has a web interface and Tauri installers.

The [synthetic demo](https://github.com/musyase/student-ai-checker#english-overview) shows the review workflow without sending documents to a model. [Unit tests run on Windows and Ubuntu](https://github.com/musyase/student-ai-checker/actions/workflows/unit-tests.yml). Grading quality still needs an independent evaluation with teacher-scored work.

[Repository](https://github.com/musyase/student-ai-checker) | [Evaluation plan](https://github.com/musyase/student-ai-checker/blob/main/docs/quality-evaluation.md)

### folder-audit

A Python command line tool that finds byte-identical files and compares folder snapshots by content. It can also produce a single HTML report that opens offline. The report lets you search file names and inspect duplicate groups. The tool never deletes files.

[Repository](https://github.com/musyase/folder-audit) | [Live sample report](https://musyase.github.io/folder-audit/demo.html) | [Tests](https://github.com/musyase/folder-audit/actions/workflows/tests.yml)

## Other work

- [Stav Electroset](https://github.com/musyase/stav-electroset-app): an Android news reader prototype in Java, with Room storage and a WordPress API fallback. Its debug build runs in CI.
- [FRVehicleDamageControl](https://github.com/musyase/FRVehicleDamageControl): a C# game plugin for changing vehicle damage settings.
