from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)

    def quit(self) -> None:
        self.app.quit()

    def copy(self) -> None:
        self.textEdit.copy()

    def cut(self) -> None:
        self.textEdit.cut()

    def paste(self) -> None:
        self.textEdit.paste()

    def undo(self) -> None:
        self.textEdit.undo()

    def redo(self) -> None:
        self.textEdit.redo()

    def about(self) -> None:
        QMessageBox.information(self,"这里是标签      ", "这里是正文      ")

    def aboutQt(self) -> None:
        QApplication.aboutQt()
