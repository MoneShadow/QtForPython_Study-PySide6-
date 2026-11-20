from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout")

        self.button1: QPushButton = QPushButton("One")
        self.button2: QPushButton = QPushButton("Two")
        self.button3: QPushButton = QPushButton("Three")
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button4: QPushButton = QPushButton("Four")
        self.button5: QPushButton = QPushButton("Five")
        self.button6: QPushButton = QPushButton("Six")
        self.button7: QPushButton = QPushButton("Seven")

        self.grid_layout: QGridLayout = QGridLayout()
        self.grid_layout.addWidget(self.button1, 0, 0)
        self.grid_layout.addWidget(self.button2, 0, 1, 1, 2)
        self.grid_layout.addWidget(self.button3, 1, 0, 2, 1)
        self.grid_layout.addWidget(self.button4, 1, 1)
        self.grid_layout.addWidget(self.button5, 1, 2)
        self.grid_layout.addWidget(self.button6, 2, 1)
        self.grid_layout.addWidget(self.button7, 2, 2)

        self.setLayout(self.grid_layout)
