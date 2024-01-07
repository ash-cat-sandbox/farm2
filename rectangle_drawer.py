from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QStackedWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect
import sys

class RectangleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rectangle Drawer")
        self.setGeometry(100, 100, 500, 500)
        self.start_point = None
        self.end_point = None
        self.rectangles = []

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            rect = QRect(self.start_point, self.end_point).normalized()
            self.rectangles.append(rect)
            self.start_point = None
            self.end_point = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(0, 0, 255))
        pen.setWidth(2)
        painter.setPen(pen)

        for rect in self.rectangles:
            painter.drawRect(rect)

        if self.start_point and self.end_point:
            current_rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(current_rect)