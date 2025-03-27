from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox Demo")
        