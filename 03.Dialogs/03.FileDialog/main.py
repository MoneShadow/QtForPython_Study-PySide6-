from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication()

window = Widget()
window.show()

app.exec()