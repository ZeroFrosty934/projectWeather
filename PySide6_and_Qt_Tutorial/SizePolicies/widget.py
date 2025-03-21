from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Size Policies and stretches")

        # Size policy : how the widgets behaves if container space is expanded or shrunk
        
        label = QLabel("Some text : ")
        line_edit = QLineEdit()

        label_0 = QLabel("Some text_0 : ")
        line_edit1 = QLineEdit()

        # Size policy : how the widgets behaves if container space is expanded or shrunk
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(label_0)
        h_layout_3.addWidget(line_edit1)
            

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        #strecth : how much of the available(in the layout) is occupied by the widget
        #You specify the stretch when you add things to the layout : button_1 takes up 2/3 of the available space
        # button_2 and button_3 take up to 1/3 of the available space

        # The number after the widget is the stretch factor
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1,2) 
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_3)
        v_layout.addLayout(h_layout_2)

