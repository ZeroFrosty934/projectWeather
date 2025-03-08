from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        # A set of signals we can connect to.
        label = QLabel("Enter your fullname: ") 
        self.line_edit = QLineEdit() # Create a QLineEdit widget.
        #self.line_edit.textChanged.connect(self.text_changed) # Connect the textChanged signal to the text_changed method.
        #self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed) # Connect the cursorPositionChanged signal to the cursor_position_changed method.
        #self.line_edit.editingFinished.connect(self.editing_finished) # Connect the editingFinished signal to the editing_finished method
        self.line_edit.returnPressed.connect(self.return_pressed) # Connect the returnPressed signal to the return_pressed method.
        #self.line_edit.selectionChanged.connect(self.selection_changed) # Connect the selectionChanged signal to the selection_changed method.
        self.line_edit.textEdited.connect(self.text_changed) # Connect the textEdited signal to the text_changed method.


        button = QPushButton("Submit")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel()

        # Create a layout and add the widgets horizontally.
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        # Create a layout and add the widgets vertically and add the horizontal layout.
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout) # Add the horizontal layout to the vertical layout.
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label) 

        self.setLayout(v_layout) # Set the layout of the widget.

    def button_clicked(self): # Method to handle the button click event.
        print("Fullname: ", self.line_edit.text()) # Print the text in the QLineEdit widget.
        self.text_holder_label.setText(self.line_edit.text()) # Set the text of the QLabel widget.

    def text_changed(self): # Method to handle the text changed event.
        self.text_holder_label.setText(self.line_edit.text()) # Set the text of the QLabel widget.

    def cursor_position_changed(self,old, new): # Method to handle the cursor position changed event.
        print("cursor old position: ", old, " -new position: ", new) 

    def editing_finished(self): # Method to handle the editing finished event.
        print("Editing finished")
        self.text_holder_label.setText(self.line_edit.text())

    def return_pressed(self): # Method to handle the return pressed event.
        print("Return pressed")
        self.text_holder_label.setText(self.line_edit.text())
    
    def selection_changed(self): # Method to handle the selection changed event.
        print("Selection changed: ", self.line_edit.selectedText())

    def text_changed(self, new_text): # Method to handle the text edited event.
        print("Text edited. new text : ", new_text)
        