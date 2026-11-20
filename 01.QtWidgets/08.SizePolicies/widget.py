from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policies")

        self.label: QLabel = QLabel("line edit")
        self.line_edit: QLineEdit = QLineEdit()
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.button1: QPushButton = QPushButton("One")
        self.button2: QPushButton = QPushButton("Two")
        self.button3: QPushButton = QPushButton("Three")

        self.hlayout1: QHBoxLayout = QHBoxLayout()
        self.hlayout1.addWidget(self.label)
        self.hlayout1.addWidget(self.line_edit)

        self.hlayout2: QHBoxLayout = QHBoxLayout()
        self.hlayout2.addWidget(self.button1, 2)
        self.hlayout2.addWidget(self.button2, 1)
        self.hlayout2.addWidget(self.button3, 1)


        self.vlayout: QVBoxLayout = QVBoxLayout()
        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addLayout(self.hlayout2)

        self.setLayout(self.vlayout)

