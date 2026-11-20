from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QToolBar, QPushButton, QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        menu_bar: QMenuBar = self.menuBar()
        file_menu: QMenu = menu_bar.addMenu("File")
        quit_action: QAction = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu: QMenu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar: QToolBar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1: QAction = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2: QAction = QAction(QIcon("QmainWindow/image.png"), "Some Other Action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        self.setStatusBar(QStatusBar(self))

        button1: QPushButton = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self) -> None:
        self.app.quit()

    def toolbar_button_click(self) -> None:
        self.statusBar().showMessage("Message from my app", 1000)

    def button1_clicked(self) -> None:
        print("Clicked on the button")