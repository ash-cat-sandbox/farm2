from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QStackedWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRect
import sys
from rectangle_drawer import RectangleDrawer

class Ui_PageSecond(QMainWindow):
       #Page2
    def setupUI(self, widget):
        self.central_widget = QWidget()
        layout = QVBoxLayout(self.central_widget)
        
        self.rectangle_drawer_button = QPushButton('Open Rectangle Drawer')
        layout.addWidget(self.rectangle_drawer_button)

        self.rectangle_drawer = None

        self.setCentralWidget(self.central_widget)  # Setting central widget

        widget.addWidget(self)

        self.rectangle_drawer_button.clicked.connect(self.showRectangleDrawer)
        
    def showRectangleDrawer(self):
        print("Button Clicked!")
        if not self.rectangle_drawer:
            self.rectangle_drawer = RectangleDrawer()
        self.rectangle_drawer.show()

    def hideEvent(self, event):
        if self.rectangle_drawer and self.rectangle_drawer.isVisible():
            self.rectangle_drawer.close()



'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RectangleDrawer()
    window.show()
    sys.exit(app.exec_())'''