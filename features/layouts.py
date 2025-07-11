from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton

def create_demo():
    widget = QWidget()
    layout = QGridLayout(widget)
    for i in range(3):
        for j in range(3):
            layout.addWidget(QPushButton(f"{i},{j}"), i, j)
    return widget