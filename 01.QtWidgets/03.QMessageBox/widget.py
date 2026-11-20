from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("QMessageBox")

        # 创建若干按键
        button_hard: QPushButton = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical: QPushButton = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question: QPushButton = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information: QPushButton = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning: QPushButton = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about: QPushButton = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        # 设置布局
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)


    #The hard way : critical
    def button_clicked_hard(self) -> None:
        message: QMessageBox = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it ?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        #Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")


    #Critical        
    def button_clicked_critical(self) -> None:
        ret: QMessageBox = QMessageBox.critical(self,"Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    #Question
    def button_clicked_question(self) -> None:
        ret: QMessageBox = QMessageBox.question(self,"Message Title", "Asking a question?", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    #Information
    def button_clicked_information(self) -> None:
        ret: QMessageBox = QMessageBox.information(self,"Message Title", "Some information", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    #Warning
    def button_clicked_warning(self) -> None:
        ret: QMessageBox = QMessageBox.warning(self,"Message Title", "Some Warning", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    #About
    def button_clicked_about(self) -> None:
        ret: QMessageBox = QMessageBox.about(self,"Message Title", "Some about message")
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")