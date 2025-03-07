from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPushButton Example")

        button = QPushButton("Click Me!!")
        button.clicked.connect(self.button_clicked) # Connect the clicked signal to the button_clicked method
        button.pressed.connect(self.button_pressed) # Connect the pressed signal to the button_pressed method
        button.released.connect(self.button_released) # Connect the released signal to the button_released method

        layout = QVBoxLayout() # Create a QVBoxLayout layout
        layout.addWidget(button) # Add the button to the layout

        self.setLayout(layout) 

    def button_clicked(self): # The clicked slot method 
        print("Button Clicked!!")
    def button_pressed(self): # The pressed slot method
        print("Button Pressed!!")
    def button_released(self): # The released slot method
        print("Button Released!!")
    
    