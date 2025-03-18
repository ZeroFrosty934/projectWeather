from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Size Policies and stretches")

        # Size policy : how the widgets behaves if container space is expanded or shrunk
        label = QLabel("Some text : ")
        label_edit = QLineEdit()

        