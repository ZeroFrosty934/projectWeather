from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("QTabWidget Demo")

        tab_widget = QTabWidget(self)


        widget_form = QWidget() # Create a widget
        label_full_name = QLabel("Full Name :")
        line_edit_full_name = QLineEdit()

        form_layout = QHBoxLayout() # Create a horizontal layout
        form_layout.addWidget(label_full_name) 
        form_layout.addWidget(line_edit_full_name)

        widget_form.setLayout(form_layout) # Set layout to widget

        # Buttons
        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.on_button_clicked)

        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)

        widget_buttons.setLayout(buttons_layout)

    def on_button_clicked(self):
        print("Button one clicked")