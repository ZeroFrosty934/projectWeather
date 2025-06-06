from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QButtonGroup


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")

        # Checkboxes : operation system
        os = QGroupBox("Choose Operation System") 

        # Create checkboxes for Windows, Linux and Mac
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled) # Connect the toggled signal to a slot

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        # Exclusive checkboxes : Drinks
        drinks = QGroupBox("Choose Your Drink") 

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        #Make the checkboxes exclusive by adding them to a QButtonGroup
        exclusive_button_group = QButtonGroup(self) # Create a QButtonGroup and set it as a self parent
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive

        drinks_layout = QVBoxLayout() # Create a vertical layout for the drinks group
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(juice)
        drinks_layout.addWidget(coffee)
        drinks.setLayout(drinks_layout)

        # Radio buttons : answers
        answers = QGroupBox("Choose Answer")
        answers_a = QRadioButton("A")
        answers_b = QRadioButton("B")
        answers_c = QRadioButton("C")
        answers_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answers_a)
        answers_layout.addWidget(answers_b)
        answers_layout.addWidget(answers_c)
        answers.setLayout(answers_layout)

        # Create a horizontal and vertical layout to add the groups
        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout) 

    # Slot functions for checkboxes
    def windows_box_toggled(self, checked):
        if(checked):
            print("Windows is checked")
        else:
            print("Windows is unchecked")
    
    def linux_box_toggled(self, checked):
        if(checked):
            print("Linux is checked")
        else:
            print("Linux is unchecked")
    
    def mac_box_toggled(self, checked):
        if(checked):
            print("Mac is checked")
        else:
            print("Mac is unchecked")