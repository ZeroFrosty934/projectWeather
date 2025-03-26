from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QListWidget, QAbstractItemView, QPushButton

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

        # Added buttons to the layout
        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.add_item)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.delete_item)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selected_items)



        # Layout for displaying the buttons on the screen
        v_layout = QVBoxLayout(self)
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_delete_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)

    def current_item_changed(self, items): # This definition is called when the current item is changed.
        print("Current item changed: ", items.text())

    def current_text_changed(self, text): # This definition is called when the current text is changed. 
        print("Current text changed: ", text)