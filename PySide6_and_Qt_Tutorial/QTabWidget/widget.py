from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("QTabWidget Demo")
