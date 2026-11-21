from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget
from infodialog import InfoDialog

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog")

        self.input_button.clicked.connect(self.input_info)

        self.info_dialog = InfoDialog()

    def input_info(self) -> None:
        ret = self.info_dialog.exec()
        if(ret == QDialog.Accepted):
            self.info_label.setText(f"你的职业是{self.info_dialog.position} 使用的系统是{self.info_dialog.using_os}")
        else:
            print("拒绝")