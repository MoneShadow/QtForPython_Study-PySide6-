from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader: QUiLoader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("02.QtDesigner/03.UsingQtDesigner_V2/widget.ui", None)
        self.ui.setWindowTitle("User Data")
        self.ui.submit_button.clicked.connect(self.do_something)

    def show(self) -> None:
        self.ui.show()

    def do_something(self) -> None:
        print(f"{self.ui.full_name_line_edit.text()} is a {self.ui.occupation_line_edit.text()}")