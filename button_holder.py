from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        button = QPushButton("Click me")

        self.setCentralWidget(button)