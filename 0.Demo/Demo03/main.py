from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data: int):
    print(f"slider moved to : {data}")

app: QApplication = QApplication()
slider: QSlider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()