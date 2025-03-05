# 1 Example of a simple button holder using a class.
""" import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        button = QPushButton("Click me")

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec_() """

# example of a button holder using a class from a different file.
""" import sys 
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder


app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec() """


# Example of a button
""" from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def button_clicked(data):
    print("Button was clicked! Checked : ", data )

app = QApplication([])
button = QPushButton("Click me")
button.setCheckable(True)


button.clicked.connect(button_clicked)

button.show()
app.exec() """


# Example of a slider
""" from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("Slider moved to : ", data )

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec() """ 


from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RocWidget
import sys

app = QApplication(sys.argv)

windows = RocWidget()
windows.show()

app.exec()

