from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton


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

        layout = QVBoxLayout()
        layout.addWidget(os)

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