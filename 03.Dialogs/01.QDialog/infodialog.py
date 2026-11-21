from PySide6.QtWidgets import QDialog
from ui_infodialog import Ui_infodialog

class InfoDialog(QDialog, Ui_infodialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("个人信息")

        #Fields
        self.position = ""
        self.using_os = ""

        #Connections
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def ok(self) -> None:
        if(not(self.occupation_lineedit.text() == '')):
            self.position = self.occupation_lineedit.text()
        self.using_os = self.selectos_combobox.currentText()
        self.accept()

    def cancel(self) -> None:
        self.reject()
