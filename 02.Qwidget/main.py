from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RocWidget
import sys

app: QApplication = QApplication(sys.argv)

window: RocWidget = RocWidget()
window.show()

app.exec()