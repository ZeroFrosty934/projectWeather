from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Example")

        self.text_edit = QTextEdit() # Create a QTextEdit object
        #self.text_edit.textChanged.connect(self.text_changed) 


        #Buttons for the QTextEdit
        copy_button = QPushButton("Copy")
        copy_button = copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("Cut")
        cut_button = cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button = paste_button.clicked.connect(self.text_edit.paste) # got through a custom slot

        undo_button = QPushButton("Undo")
        undo_button = undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button = redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button = set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set HTML")
        set_html_button = set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        clear_button = clear_button.clicked.connect(self.text_edit.clear)