from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar #import the required classes from the QtWidgets module
from PySide6.QtCore import QSize #import the QSize class from QtCore module
from PySide6.QtGui import QAction, QIcon #import the QAction and QIcon classes from the QtGui module

class MainWindow(QMainWindow): #create a class(MainWindow) that inherits from QMainWindow 
    def __init__(self, app): # add app as a parameter to the constructor from QMainWindow 
        super().__init__() #call the parent constructor from QMainWindow 

        self.app = app #declare an app member 
        self.setWindowTitle("Custom MainWindow") #set the window title
        self.menuBar().setNativeMenuBar(False) #set the native menubar to false to display the menubar for macOS

        #menubar and menu
        menu_bar = self.menuBar() #create a menubar
        file_menu = menu_bar.addMenu("File") #create a menu for "File"

        quit_action = file_menu.addAction("Quit") # add an action to the menu
        quit_action.triggered.connect(self.quit_app) #connect the action to a slot

        edit_menu = menu_bar.addMenu("Edit") #create a menu for "Edit"
        edit_menu_copy_pressed = edit_menu.addAction("Copy") # add an action to the menu
        edit_menu_copy_pressed.triggered.connect(self.edit_menu_copy_pressed) #connect the action to a slot


        edit_menu_cut_pressed = edit_menu.addAction("Cut") 
        edit_menu_cut_pressed.triggered.connect(self.edit_menu_cut_pressed) 

        edit_menu_paste_pressed = edit_menu.addAction("Paste")
        edit_menu_paste_pressed.triggered.connect(self.edit_menu_paste_pressed)

        edit_menu_undo_pressed = edit_menu.addAction("Undo")
        edit_menu_undo_pressed.triggered.connect(self.edit_menu_undo_pressed)

        edit_menu_redo_pressed = edit_menu.addAction("Redo")
        edit_menu_redo_pressed.triggered.connect(self.edit_menu_redo_pressed)

        # add more menus here
        menu_bar.addMenu("View")
        menu_bar.addMenu("Help")
        menu_bar.addMenu("Settings")

        # Add toolbars
        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Add toolbar actions
        toolbar.addAction(quit_action)

       
        action1 = QAction("Some Action", self) #create an action
        action1.setStatusTip("Status message for some action") #set the status tip for the action
        action1.triggered.connect(self.toolbar_button_clicked) #connect the action to a slot
        toolbar.addAction(action1) # add the action to the toolbar

        action2 = QAction(QIcon("start.png"), "Some other action", self) #create an action with an icon
        action2.setStatusTip("Status message for some other action") #set the status tip for the action
        action2.triggered.connect(self.toolbar_button_clicked) #connect the action to a slot
        #action2.setCheckable(True) #set the action to be checkable
        toolbar.addAction(action2) # add the action to the toolbar

        toolbar.addSeparator() # add a separator to the toolbar
        toolbar.addWidget(QPushButton("Click here")) # add a button to the toolbar
        toolbar.addWidget(QPushButton("Click here2"))
        toolbar.addSeparator()
        
        # Working with status bar
        self.setStatusBar(QStatusBar(self)) #create a status bar and set it to the main window

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked) #connect the button to a slot so that when it is clicked, the slot is called.
        self.setCentralWidget(button1) #set the central widget to the button so that it is displayed in the center of the window. 




    def quit_app(self): #create a slot
        self.app.quit() #quit the application

    def toolbar_button_clicked(self): 
        self.statusBar().showMessage("Message from my app", 2000) #show a message in the status bar for 2 seconds

    def button1_clicked(self): # method to handle the button click event.
        print("Button 1 clicked") 

    def edit_menu_copy_pressed(self): #method to handle the copy action from the edit menu.
        print("Copy pressed") #print a message to the console

    def edit_menu_cut_pressed(self): 
        print("Cut pressed") 
    
    def edit_menu_paste_pressed(self): 
        print("Paste pressed")
    
    def edit_menu_undo_pressed(self): 
        print("Undo pressed")
    
    def edit_menu_redo_pressed(self): 
        print("Redo pressed")