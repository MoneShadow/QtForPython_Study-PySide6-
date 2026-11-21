from PySide6.QtWidgets import QApplication
from mianwindow import MainWindow

app: QApplication = QApplication()
window: MainWindow = MainWindow(app)
window.show()

app.exec()