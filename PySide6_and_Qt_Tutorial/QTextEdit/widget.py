from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Example")

        self.text_edit = QTextEdit() # Create a QTextEdit object
        #self.text_edit.textChanged.connect(self.text_changed) 


        # Create buttons for the QTextEdit.

        current_text_button = QPushButton("Current Text")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy) # Connect directly to the QTextEdit slot. 

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste) # got through a custom slot

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set Plain Text")
        #set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set HTML")
        #set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        #clear_button = clear_button.clicked.connect(self.text_edit.clear)

        # Create horizontal layout for the buttons.
        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        # Create vertical layout for the QTextEdit and the buttons. 
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)
        
        self.setLayout(v_layout)
    
    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText()) # Print the current text in terminal when the button is clicked. 

