from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

def create_demo():
    widget = QWidget()
    btn = QPushButton("Emit Signal")
    btn.clicked.connect(lambda: print("Button clicked!"))
    layout = QVBoxLayout(widget)
    layout.addWidget(btn)
    return widget