from PySide6.QtWidgets import QApplication
from widget import *

app: QApplication = QApplication()
window: Widget = Widget()
window.show()

app.exec()