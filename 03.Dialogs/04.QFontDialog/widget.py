from PySide6.QtWidgets import QWidget, QFontDialog
from PySide6.QtGui import QFont
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFontDialog")
        self.button.clicked.connect(self.button_cliked)

    def button_cliked(self) -> None:
        ok, font = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 20), self)
        if ok:
            self.label.setFont(font)
        else:
            print("User did't select any valid font")
        