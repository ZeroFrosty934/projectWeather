from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QLabel Images")

        image_label = QLabel() # Create a QLabel object
        image_label.setPixmap(QPixmap("images/Cat_Riding_horse.jpg")) # Set the image to be displayed and the path to the image.

        layout = QVBoxLayout() 
        layout.addWidget(image_label) # Add the QLabel object to the layout

        self.setLayout(layout)