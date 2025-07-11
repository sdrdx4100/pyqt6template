from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

def create_demo():
    widget = QWidget()
    layout = QVBoxLayout(widget)

    label = QLabel("Hello, PySide6!")
    button = QPushButton("Click me")
    layout.addWidget(label)
    layout.addWidget(button)

    return widget