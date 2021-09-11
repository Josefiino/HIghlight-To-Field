# -*- coding: utf-8 -*-

import re
from anki import collection
from aqt import mw, gui_hooks
from aqt.operations import CollectionOp
from aqt.qt import *
from aqt.utils import shortcut, showInfo
from aqt.main import ResetReason

#Get the config setup
config = mw.addonManager.getConfig(__name__)
field_1 = config['field_1']
shortcut_1 = config['shortcut_1']
field_2 = config['field_2']
shortcut_2 = config['shortcut_2']
field_3 = config['field_3']
shortcut_3 = config['shortcut_3']
field_4 = config['field_4']
shortcut_4 = config['shortcut_4']

# Class to cointain the functions
class htf(object): # htf = highlight to field
    def __init__(self):
        pass 

    def dummy(self):
        #showInfo("Dummy worked!")
        notes = mw.reviewer.card.note
        showInfo(f"field content = {notes[field_1]}")
        # notes[field_1] += "CARALHO"
        # notes.flush()
        

    def get_highlight(self):
        selection = mw.web.selectedText()
        selection = selection.strip()
        if not selection:
            showInfo("There is no highlighted text")
            return
        if "\n" in selection:
            showInfo("Can't look text with newline characters")
            return
        return selection

    def get_note_info(self): # Gets the info from the note to be updated
        cir = mw.reviewer.card # cir = Card in Reviewer
        try:
            noteid = cir.nid # Gets the note ID from cir
            note = mw.col.getNote(noteid) # Gets note info from the ID
        except:
            showInfo("No card is being reviewed")
            return     
        return note
        # showInfo(f"noteid = {noteid}\n"
        #          f"note = {note}\n"
        #          f"focus note = {note['Focus']}")

    def update_field(self, field):  # Gets the highlighted text and updates the called 
                                    # field of the current note        
        content = self.get_highlight()
        if content: # Check if content has something before doing the field update
            note = self.get_note_info()
            try: # Checks if the field name exists
                note[field] = content 
            except:
                showInfo(f"No field called {field}. Please set a valid one in the config.")
            note.flush()
            mw.requireReset(reason=ResetReason.EditCurrentInit)
            mw.delayedMaybeReset()
        else:
            return 

# Add the menu and options
def add_menu():
    mh = QMenu()
    mh.setTitle("Highlight To Field")
    mw.form.menuTools.addAction(mh.menuAction())
    mw.form.menuHighlight = mh
    # Adding actions
    # Action for shorcut 1
    a = QAction(mw)
    a.setText(f"Update {field_1} ")
    a.setShortcut(shortcut_1)
    mh.addAction(a)
    a.triggered.connect(lambda: htf().update_field(field_1))
    # Action for shorcut 2
    a = QAction(mw)
    a.setText(f"Update {field_2} ")
    a.setShortcut(shortcut_2)
    mh.addAction(a)
    a.triggered.connect(lambda: htf().update_field(field_2))
    # Action for shorcut 3
    a = QAction(mw)
    a.setText(f"Update {field_3} ")
    a.setShortcut(shortcut_3)
    mh.addAction(a)
    a.triggered.connect(lambda: htf().update_field(field_3))
    # Action for shorcut 4
    a = QAction(mw)
    a.setText(f"Update {field_4} ")
    a.setShortcut(shortcut_4)
    mh.addAction(a)
    a.triggered.connect(lambda: htf().update_field(field_4))

add_menu()
