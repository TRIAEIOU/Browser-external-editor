# Browser external editor
Minimal implementation Anki addon (https://ankiweb.net/shared/info/2065559429) to open note(s) in separate window(s) from the browser.

**\*\*\*\* All credit goes to Glutanimate (https://github.com/Glutanimate/) for the concept, this is just a minimal implementation written from scratch that works with current Anki (2.1.49 at the time of writing) \*\*\*\***

## Remarks
- Available from context menu in browser as well as keyboard shortcut `Ctrl+Alt+E` (configurable in Qt format, see https://doc.qt.io/qt-5/qkeysequence.html).
- Supports multiple windows of the same note open as well as multiple windows of different notes but uses a single stored geometry (the same as for the Edit current note available from the reviewer).
- Support thread Anki forum https://forums.ankiweb.net/t/browser-external-editor-support-thread/17223.
- Very minimal wrapper around the core Anki "Edit current note" dialog (available from review).
- "Continuous note autosync with DB" is disabled for the external editor windows which means the note is not updated in the editor if it is saved elsewhere while the window open. This is due to Anki implementation of Edit current note/Browser editor which results in the caret position being reset to the beginning of the field on every sync (which occurs every few seconds). It is therefore impractical to _edit_ the same note in several windows simultaneously as:
  - If browser editor is open with the same note that editor will still autosync-and-reset-caret.
  - Having the same note open in separate external windows will lead to the version written to the DB be the one from the window that is closed last.
