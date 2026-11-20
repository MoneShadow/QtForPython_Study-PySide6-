from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QTabWidget, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget")

        self.tab_widget: QTabWidget = QTabWidget()

        # Information
        self.widget_form: QWidget = QWidget()
        self.label_full_name: QLabel = QLabel("Some message")
        self.line_edit_full_name: QLabel = QLineEdit()

        self.Hform_layout: QHBoxLayout = QHBoxLayout()
        self.Hform_layout.addWidget(self.label_full_name)
        self.Hform_layout.addWidget(self.line_edit_full_name)
        self.widget_form.setLayout(self.Hform_layout)

        # Buttons
        self.widget_buttons: QWidget = QWidget()
        self.button1: QPushButton = QPushButton("One")
        self.button2: QPushButton = QPushButton("Two")
        self.button3: QPushButton = QPushButton("Three")

        self.Vbuttons_layout: QVBoxLayout = QVBoxLayout()
        self.Vbuttons_layout.addWidget(self.button1)
        self.Vbuttons_layout.addWidget(self.button2)
        self.Vbuttons_layout.addWidget(self.button3)
        self.widget_buttons.setLayout(self.Vbuttons_layout)

        # Add tabs
        self.tab_widget.addTab(self.widget_form, "Information")
        self.tab_widget.addTab(self.widget_buttons, "Buttons")

        # 总布局
        self.total_layout = QVBoxLayout()
        self.total_layout.addWidget(self.tab_widget)

        self.setLayout(self.total_layout)