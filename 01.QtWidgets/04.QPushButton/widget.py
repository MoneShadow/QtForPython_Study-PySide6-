from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("主窗口")

        # 创建按键
        button: QPushButton = QPushButton("按键1")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        # 设置布局 将按键添加到窗口内容中
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(button)

        # 装载布局属性
        self.setLayout(layout)

    def button_clicked(self) -> None:
        print("Clicked")

    def button_pressed(self) -> None: 
        print("Pressed")
        
    def button_released(self) -> None:
        print("Released")