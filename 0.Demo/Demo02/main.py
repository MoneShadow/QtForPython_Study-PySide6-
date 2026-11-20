from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data: bool):
    print("按键按下", data)

app: QApplication = QApplication()
button: QPushButton = QPushButton()

button.setText("Press Me")
button.setCheckable(True)
button.clicked.connect(button_clicked)

button.show()
app.exec()