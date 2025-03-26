from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QListWidget, QAbstractItemView

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Demo")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One") # Add one item to the list
        self.list_widget.addItems(["Two", "Three"]) # Add multiple items to the list at once.

        self.list_widget.currentItemChanged.connect(self.current_item_changed) # Connect the current item changed signal to the current_item_changed definition.
        self.list_widget.currentTextChanged.connect(self.current_text_changed) # Connect the current text changed signal to the current_text_changed definition.


        v_layout = QVBoxLayout(self)
        v_layout.addWidget(self.list_widget)

        self.setLayout(v_layout)

    def current_item_changed(self, items): # This definition is called when the current item is changed.
        print("Current item changed: ", items.text())

    def current_text_changed(self, text): # This definition is called when the current text is changed. 
        print("Current text changed: ", text)