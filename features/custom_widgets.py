from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("skyblue"))

def create_demo():
    return MyWidget()