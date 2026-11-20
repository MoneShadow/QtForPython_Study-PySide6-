from PySide6 import QtWidgets
from user_interface import UserInterface

app: QtWidgets.QApplication = QtWidgets.QApplication()

window = UserInterface()
window.show()

app.exec()