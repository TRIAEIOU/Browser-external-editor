from aqt.editcurrent import *

class BrowserExternalEditor(EditCurrent):
    def __init__(self, mw, browser: aqt.browser.Browser) -> None:
        QDialog.__init__(self, None, Qt.WindowType.Window)
        mw.garbage_collect_on_dialog_finish(self)
        self.mw = mw
        self.form = aqt.forms.editcurrent.Ui_Dialog()
        self.form.setupUi(self)
        self.setWindowTitle(tr.editing_edit_current())
        disable_help_button(self)
        self.setMinimumHeight(400)
        self.setMinimumWidth(250)
        self.form.buttonBox.button(QDialogButtonBox.StandardButton.Close).setShortcut(
            QKeySequence("Ctrl+Return")
        )
        self.editor = aqt.editor.Editor(self.mw, self.form.fieldsArea, self)
        #self.editor.card = self.mw.reviewer.card # Anki source
        #self.editor.set_note(self.mw.reviewer.card.note(), focusTo=0) # Anki source
        #restoreGeom(self, "editcurrent") # Anki source
        self.editor.card = browser.card # Browser external editor
        self.editor.set_note(self.editor.card.note(), focusTo=0) # Browser external editor
        restoreGeom(self, "browserexternaleditor") # Browser external editor
        gui_hooks.operation_did_execute.append(self.on_operation_did_execute)
        self.show()


BEE_TITLE = "Browser external editor"
BEE_MENU = "Open in external editor"
CFG_SC_EDIT = "Shortcut"
BEE_SC_EDIT = None

def setup_shortcuts(browser: aqt.browser.Browser):
    config = browser.mw.addonManager.getConfig(__name__)
    BEE_SC_EDIT = config.get(CFG_SC_EDIT)
    if BEE_SC_EDIT:
        sc = QShortcut(QKeySequence(BEE_SC_EDIT), browser)
        sc.activated.connect(lambda: BrowserExternalEditor(browser.mw, browser))

#def setup_menu(browser: aqt.browser.Browser):
def setup_menu(browser: aqt.browser.Browser, menu: QMenu):
    label = BEE_MENU
    if BEE_SC_EDIT:
        label = f"{BEE_MENU} ({BEE_SC_EDIT})"
    action = QAction(label, browser)
    action.triggered.connect(lambda: BrowserExternalEditor(browser.mw, browser))
    menu.addAction(action)

gui_hooks.browser_will_show.append(setup_shortcuts)
gui_hooks.browser_will_show_context_menu.append(setup_menu)
