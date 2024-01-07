from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap, QColor, QCursor
from PyQt5.QtCore import Qt, QRect

class CropAdd(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.rectangles = []  # Store rectangles' positions and sizes
        self.rect_width = 50
        self.rect_height = 50
        self.cursor_pixmap = self.create_cursor_pixmap()

    def create_cursor_pixmap(self):
        # Create a pixmap with the dimensions of the rectangle
        pixmap = QPixmap(self.rect_width, self.rect_height)
        pixmap.fill(Qt.transparent) # Set pixmap background

        # Draw a rectangle in the pixmap
        painter = QPainter(pixmap)
        painter.setPen(QColor(Qt.black))
        painter.drawRect(0, 0, self.rect_width -1, self.rect_height - 1)
        painter.end()

        return pixmap

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
            rect_width = 50
            rect_height = 50
            rect = QRect(event.pos().x() - rect_width // 2, event.pos().y() - rect_height // 2, rect_width, rect_height)
            self.rectangles.append(rect)
            self.update()  # Refresh the widget to display the new rectangle

    def mouseMoveEvent(self, event):
        # change cursor
        self.setCursor(QCursor(self.cursor_pixmap))
        event.accept()
        '''cursor_rect = QRect(event.pos().x(), event.pos().y(), self.rect_width, self.rect_height)
        if any(cursor_rect.intersects(rect) for rect in self.rectangles): # Cursor changes to "Forbidden" if hovering over existing rectangles
            self.setCursor(Qt.ForbiddenCursor)
        else:
            self.setCursor(Qt.CrossCursor)    '''
