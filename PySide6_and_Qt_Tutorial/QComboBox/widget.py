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


        # Create a layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_value)
        v_layout.addWidget(button_get_value)

        self.setLayout(v_layout)

    
    # Adding methods to the class
    def get_current_value(self): # Get the current value of the ComboBox
        print("Current value : ", self.combo_box.currentText(),
              " - current index : ", self.combo_box.currentIndex())

    def set_value(self): # Set the value of the ComboBox
        self.combo_box.setCurrentIndex(2)

    def get_value(self): # Get all the values in the ComboBox
        for i in range(self.combo_box.count()):
            print("Index [", i, "] : ", self.combo_box.itemText(i))