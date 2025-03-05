from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RocKWidget")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button1.clicked.connect(self.button1_clicked)
        button_layout.addWidget(button2)
        button2.clicked.connect(self.button2_clicked)
        button_layout.addWidget(button3)
        button3.clicked.connect(self.button3_clicked)
        button_layout.addWidget(button4)
        button4.clicked.connect(self.button4_clicked)
        button_layout.addWidget(button5)
        button5.clicked.connect(self.button5_clicked)

        self.setLayout(button_layout)
    
    def button1_clicked(self):
        print("Button1 was clicked!")

    def button2_clicked(self):
        print("Button2 was clicked!")
    
    def button3_clicked(self):
        print("Button3 was clicked!")
    
    def button4_clicked(self):
        print("Button4 was clicked!")
    
    def button5_clicked(self):
        print("Button5 was clicked!")