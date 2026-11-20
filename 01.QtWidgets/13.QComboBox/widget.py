from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QPushButton, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox")

        self.combo_box: QComboBox = QComboBox()
        #Add planets to the combobox
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Pluton")
        self.combo_box.addItem("Saturn")

        self.line_edit: QLineEdit = QLineEdit()
        self.line_edit.returnPressed.connect(self.set_current)

        self.button_current_value: QPushButton = QPushButton("Current Value")
        self.button_current_value.clicked.connect(self.current_value)
        self.button_set_current: QPushButton = QPushButton("Set value")
        self.button_set_current.clicked.connect(self.set_current)
        self.button_get_values: QPushButton = QPushButton("Get values")
        self.button_get_values.clicked.connect(self.get_values)

        self.h_layout: QHBoxLayout = QHBoxLayout()
        self.h_layout.addWidget(self.line_edit)
        self.h_layout.addWidget(self.button_set_current)


        self.v_layout: QVBoxLayout = QVBoxLayout()
        self.v_layout.addWidget(self.combo_box)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.button_current_value)
        self.v_layout.addWidget(self.button_get_values)
    
        self.setLayout(self.v_layout)

    def current_value(self) -> None:
        print(f"Current item : {self.combo_box.currentText()}\r\ncurrent index : {self.combo_box.currentIndex()}")

    def set_current(self) -> None:
        index: str = self.line_edit.text()
        self.line_edit.clear()
        self.combo_box.setCurrentIndex(int(index))

    def get_values(self) -> None:
        for i in range(self.combo_box.count()):
            print (f"index [{i}] : {self.combo_box.itemText(i)}")