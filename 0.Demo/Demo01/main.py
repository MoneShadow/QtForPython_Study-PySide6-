import sys
from PySide6.QtWidgets import QApplication
from Demo01.button_hoder import *

app: QApplication = QApplication(sys.argv)

window: ButtonHolder = ButtonHolder()
window.show()
app.exec()
