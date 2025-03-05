from PySide6.QtWidgets import QApplication, QMainWindow #import the required classes


class MainWindow(QMainWindow):
    def __init__(self, app): # add app as a parameter to the constructor from QMainWindow 
        super().__init__() #call the parent constructor from QMainWindow

        self.app = app #declare an app member  
        self.setWindowTitle("Custom MainWindow") #set the window title