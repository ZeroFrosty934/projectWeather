from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Size Policies and stretches")

        # Size policy : how the widgets behaves if container space is expanded or shrunk
        label = QLabel("Some text : ")
        label_edit = QLineEdit()

        h_layout = QHBoxLayout()
        h_layout1.addWidget(label)
        h_layout1.addWidget(label_edit)
        

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        #strecth : how much of the available(in the layout) is occupied by the widget
        #You specify the stretch when you add things to the layout : button_1 takes up 2/3 of the available space
        # button_2 and button_3 take up to 1/3 of the available space
        
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1,2)
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)