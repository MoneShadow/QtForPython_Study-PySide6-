from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QAbstractItemView, QPushButton, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget")

        self.list_widget: QListWidget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two", "Three"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        self.button_add_item = QPushButton("Add Item")
        self.button_add_item.clicked.connect(self.add_item)

        self.button_delete_item = QPushButton("Delete Item")
        self.button_delete_item.clicked.connect(self.delete_item)

        self.button_item_count = QPushButton("Item Count")
        self.button_item_count.clicked.connect(self.item_count)

        self.button_selected_items = QPushButton("Selected Items")
        self.button_selected_items.clicked.connect(self.selected_items)

        self.line_edit: QLineEdit = QLineEdit()
        self.line_edit.returnPressed.connect(self.add_item)

        self.HLayout: QHBoxLayout = QHBoxLayout()
        self.HLayout.addWidget(self.line_edit)
        self.HLayout.addWidget(self.button_add_item)

        self.VLayout: QVBoxLayout = QVBoxLayout()
        self.VLayout.addWidget(self.list_widget)
        self.VLayout.addLayout(self.HLayout)
        self.VLayout.addWidget(self.button_delete_item)
        self.VLayout.addWidget(self.button_item_count)
        self.VLayout.addWidget(self.button_selected_items)

        self.setLayout(self.VLayout)

    def current_item_changed(self, item):
        print(f"Current item : {item.text()}")

    def current_text_changed(self,text):
        print(f"Current text changed : {text}")

    def add_item(self):
        new_item: str = self.line_edit.text()
        self.line_edit.clear()
        self.list_widget.addItem(new_item)

    def item_count(self):
        print(f"Item count : {self.list_widget.count()}")

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def selected_items(self):
        list = self.list_widget.selectedItems()
        for i in list : 
            print(i.text())