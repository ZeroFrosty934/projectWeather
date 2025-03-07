from PySide6.QtWidgets import QMessageBox, QPushButton, QPushButton, QWidget, QVBoxLayout 

class Widget(QWidget): # Create a class that inherits from QWidget
    def __init__(self): 
        super().__init__() 

        self.setWindowTitle("QMessageBox") # Set the window title

        # Set up the buttons and connect them to functions
        button_hard = QPushButton("Hard") # Create a button
        button_hard.clicked.connect(self.button_clicked_hard) # Connect the button to a function

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_infomation = QPushButton("Information")
        button_infomation.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        # Set up the layouts and add the buttons
        layout = QVBoxLayout() # Create a layout vertically
        layout.addWidget(button_hard) # Add the button to the layout
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_infomation)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout) # Set the layout for the widget

    # Define the functions that will be called when the buttons are clicked
    def button_clicked_hard(self):
        message = QMessageBox() # Create a message box
        message.setMinimumSize(700,200) # Set the minimum size of the message box
        message.setWindowTitle("Hard") # Set the title of the message box
        message.setText("This is a hard message") # Set the text of the message box
        message.setInformativeText("Do you want to do something about it?") # Set the informative text of the message box
        message.setIcon(QMessageBox.Critical) # Set the icon of the message box
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) # Set the standard buttons of the message box
        message.setDefaultButton(QMessageBox.Ok) # Set the default button of the message box
        # Show the message box and get the return value
        ret = message.exec() 
        if ret == QMessageBox.Ok : # Check the return value
            print("Ok")
        else:
            print("Cancel")
        
    # Critical message box with save, discard, and cancel buttons 
    def button_clicked_critical(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("This is a critical message")
        msgBox.setWindowTitle("Critical")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec()
        if ret == QMessageBox.Save:
            print("Save")
        elif ret == QMessageBox.Discard:
            print("Discard")
        else:
            print("Cancel")

    # Question message box 
    def button_clicked_question(self):
        ret = QMessageBox.question(self, "Question", 
            "This is a question message", 
            QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")
        
    # Information message box
    def button_clicked_information(self):
        ret = QMessageBox.information(self, "Information", "This is an information message", QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")
    
    # Warning message box
    def button_clicked_warning(self, s):
        ret = QMessageBox.warning(
            self, 
            "Warning", 
            "This is a warning message", 
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
            )
        
        if ret == QMessageBox.Discard:
            print("Discard")
        elif ret == QMessageBox.NoToAll:
            print("NoToAll")
        else:
            print("Ignore")
    
    # About message box
    def button_clicked_about(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("This is an about message")
        msgBox.setWindowTitle("About")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)

        ret = msgBox.exec()
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")
