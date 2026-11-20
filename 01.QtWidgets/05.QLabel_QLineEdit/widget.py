from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("Label and LineEdit")

        # 添加标签
        label: QLabel = QLabel("Fullname : ")
        self.line_edit: QLineEdit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)                         # 编辑框文本发生变化
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)    # 光标位置改变
        # self.line_edit.editingFinished.connect(self.editing_finished)                 # 编辑完成
        # self.line_edit.returnPressed.connect(self.return_pressed)                     # 编辑完成
        # self.line_edit.selectionChanged.connect(self.selection_changed)               # 选择改变
        self.line_edit.textEdited.connect(self.text_edited)                             # 文本发生编辑

        # 添加按键
        button: QPushButton = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        # 添加标签
        self.text_holder_label: QLabel = QLabel("I AM HERE")

        # 标签和行编辑水平分布
        h_layout: QHBoxLayout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        # 其余组件垂直分布
        v_layout: QVBoxLayout = QVBoxLayout()
        v_layout.addLayout(h_layout)    # 将水平分布纳入垂直分布中
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        # 装配布局属性
        self.setLayout(v_layout)

    # Slots
    def button_clicked(self) -> None:
        print(f"Fullname : {self.line_edit.text()}")
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self) -> None:
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new) -> None:
        print(f"cursor old position : {old} new position : {new}")

    def editing_finished(self) -> None: 
        print("Editing finished")

    def return_pressed(self) -> None:
        print("Return pressed")

    def selection_changed(self) -> None:
        print(f"Selection Changed : {self.line_edit.selectedText()}")

    def text_edited(self,new_text) -> None: 
        print(f"Text edited. New text : {new_text}")