from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from ui_infodialog import Ui_infodialog

class InfoDialog(QDialog, Ui_infodialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("个人信息")

        #Fields
        self.position = ""
        self.using_os = ""

        self.button_box.clicked.connect(self.button_box_clicked)

    def button_box_clicked(self, button) -> None:
        std_button = self.button_box.standardButton(button)
        if (std_button == QDialogButtonBox.Ok):
            print("Ok")
            if (not (self.occupation_lineedit.text() == '')):
                self.position = self.occupation_lineedit.text()
            self.using_os = self.selectos_combobox.currentText()
            self.accept()
        elif (std_button == QDialogButtonBox.Cancel):
            print("Cancel")
            self.reject()
        elif (std_button == QDialogButtonBox.Save):
            print("Save")
            QMessageBox.information(self, "提示", "保存成功")
        elif (std_button == QDialogButtonBox.SaveAll):
            print("SaveAll")
            QMessageBox.information(self, "提示", "保存成功")
        elif (std_button == QDialogButtonBox.Open):
            print("Open")
            QMessageBox.information(self, "提示", "打开成功")
        else:
            print("其他按钮")

