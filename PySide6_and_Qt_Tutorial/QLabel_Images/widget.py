from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QLabel Images")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/Cat_Riding_horse.jpg"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)    