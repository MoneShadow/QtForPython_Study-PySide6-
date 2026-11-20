from PySide6.QtWidgets import QApplication
from mainwindow import *
import sys

app: QApplication = QApplication(sys.argv)
window: MainWindow = MainWindow(app)
window.show()

app.exec()