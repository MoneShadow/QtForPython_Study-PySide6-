from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader: QUiLoader = QUiLoader()

app: QtWidgets.QApplication = QtWidgets.QApplication()
window: QtWidgets.QWidget = loader.load("02.QtDesigner/02.UsingQtDesigner/widget.ui", None)

def do_someting() -> None:
    print(f"{window.full_name_line_edit.text()} is a {window.occupation_line_edit.text()}")

window.setWindowTitle("User data")

window.submit_button.clicked.connect(do_someting)
window.show()
app.exec()