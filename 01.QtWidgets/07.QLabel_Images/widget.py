from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Images")

        image_label: QLabel = QLabel()
        image_label.setPixmap(QPixmap("/home/mone/Project/pyside6_qt6_turtorial/7.QLabel_Images/image.png"))

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)