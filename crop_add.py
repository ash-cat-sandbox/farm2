from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect

class CropAdd(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.rectangles = []  # Store rectangles' positions and sizes

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(0, 0, 255, 100))  # Semi-transparent blue color
        painter.setBrush(brush)

        for rect in self.rectangles:
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Create a rectangle with a specific size (e.g., 100x50) at the clicked position
            rect_width = 100
            rect_height = 50
            rect = QRect(event.pos().x(), event.pos().y(), rect_width, rect_height)
            self.rectangles.append(rect)
            self.update()  # Refresh the widget to display the new rectangle
