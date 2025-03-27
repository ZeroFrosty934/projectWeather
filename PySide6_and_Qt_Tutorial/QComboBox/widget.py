from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.setWindowTitle("QComboBox Demo")

        # Add planets to the ComboBox widget.
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Saturn")


        # Buttons
        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.get_current_value)

        button_set_value = QPushButton("Set Value")
        button_set_value.clicked.connect(self.set_value)

        button_get_value = QPushButton("Get Value")
        button_get_value.clicked.connect(self.get_value)