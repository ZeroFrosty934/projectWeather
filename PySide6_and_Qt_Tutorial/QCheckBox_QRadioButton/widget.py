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
        drinks_layout.addWidget(juice)
        drinks_layout.addWidget(coffee)
        drinks.setLayout(drinks_layout)

        # Create a horizontal layout and add the two groups
        layout = QHBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drinks)

        self.setLayout(layout) 
        
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