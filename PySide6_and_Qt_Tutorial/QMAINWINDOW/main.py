from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv) #create the application

window = MainWindow(app) #create the main window
window.show() #display the main window

app.exec() #execute the application
