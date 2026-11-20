from PySide6.QtWidgets import QWidget, QGroupBox, QCheckBox, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")

        # 系统
        self.os: QGroupBox = QGroupBox("选择您的操作系统")

        self.windows: QCheckBox = QCheckBox("Windows")
        self.windows.toggled.connect(self.windows_box_toggled)
        self.linux: QCheckBox = QCheckBox("Linux")
        self.linux.toggled.connect(self.linux_box_toggled)
        self.mac: QCheckBox = QCheckBox("Mac")
        self.mac.toggled.connect(self.mac_box_toggled)

        self.os_layout: QVBoxLayout = QVBoxLayout()
        self.os_layout.addWidget(self.windows)
        self.os_layout.addWidget(self.linux)
        self.os_layout.addWidget(self.mac)
        self.os.setLayout(self.os_layout)

        # 饮品
        self.drink: QGroupBox = QGroupBox("选择您的饮品(单选)")

        self.beer: QCheckBox = QCheckBox("啤酒")
        self.juice: QCheckBox = QCheckBox("果汁")
        self.coffe: QCheckBox = QCheckBox("咖啡")
        self.beer.setChecked(True)

        # 互斥复选框
        self.exclusive_button_group: QButtonGroup = QButtonGroup(self) # The self parent is needed here.
        self.exclusive_button_group.addButton(self.beer)
        self.exclusive_button_group.addButton(self.juice)
        self.exclusive_button_group.addButton(self.coffe)
        self.exclusive_button_group.setExclusive(True)

        self.drink_layout: QVBoxLayout = QVBoxLayout()
        self.drink_layout.addWidget(self.beer)
        self.drink_layout.addWidget(self.juice)
        self.drink_layout.addWidget(self.coffe)
        self.drink.setLayout(self.drink_layout)

        # 选项
        self.answers: QGroupBox = QGroupBox("Choose Answer")

        # 单选按钮
        self.answer_a: QRadioButton = QRadioButton("A")
        self.answer_b: QRadioButton = QRadioButton("B")
        self.answer_c: QRadioButton = QRadioButton("C")
        self.answer_a.setChecked(True)

        self.answers_layout: QVBoxLayout = QVBoxLayout()
        self.answers_layout.addWidget(self.answer_a)
        self.answers_layout.addWidget(self.answer_b)
        self.answers_layout.addWidget(self.answer_c)
        self.answers.setLayout(self.answers_layout)

        # 总布局
        self.HBOXlayout: QHBoxLayout =  QHBoxLayout()
        self.HBOXlayout.addWidget(self.os)
        self.HBOXlayout.addWidget(self.drink)

        self.VBOXlayout: QVBoxLayout = QVBoxLayout()
        self.VBOXlayout.addLayout(self.HBOXlayout)
        self.VBOXlayout.addWidget(self.answers)
        
        self.setLayout(self.VBOXlayout)

    def windows_box_toggled(self,checked): 
            if(checked):
                print("Windows box checked")
            else:
                print("Windows box unchecked")

    def linux_box_toggled(self,checked): 
            if(checked):
                print("Linux box checked")
            else:
                print("Linux box unchecked")

    def mac_box_toggled(self,checked): 
            if(checked):
                print("Mac box checked")
            else:
                print("Mac box unchecked")
