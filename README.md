# Browser external editor

## ** All credit goes to Glutanimate (https://github.com/Glutanimate/) for the idea, I just did a minimal implementation from scratch that works with current Anki (2.1.49 at the time of writing) **

Minimal implementation Anki addon (https://ankiweb.net/shared/info/2065559429) to open note(s) in separate window(s) from the browser. Anki forum https://forums.ankiweb.net/t/editor-js-snippets-support-thread/14958).
- Very minimal wrapper around the core Anki "Edit current note" dialog (available from review).
- Available from context menu in browser as well as keyboard shortcut `Ctrl+Alt+E` (configurable in Qt format, see https://doc.qt.io/qt-5/qkeysequence.html).
- Supports multiple windows of the same note open as well as multiple windows of different notes.
