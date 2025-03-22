from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GridLayout Demo")

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        #button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")