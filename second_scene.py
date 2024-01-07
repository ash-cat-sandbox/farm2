from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QStackedWidget
from PyQt5.QtGui import QPainter, QColor, QCursor
from PyQt5.QtCore import Qt, QRect
import subprocess
from rectangle_drawer import RectangleDrawer
from crop_add import CropAdd

class Ui_PageSecond(QMainWindow):
       #Page2
    def setupUI(self, widget):
        self.central_widget = QWidget()
        layout = QVBoxLayout(self.central_widget)
        
        self.rectangle_drawer_button = QPushButton('Open Rectangle Drawer')
        layout.addWidget(self.rectangle_drawer_button)

        self.crop_add_button = QPushButton('Add Crop')
        layout.addWidget(self.crop_add_button)

        self.clear_button = QPushButton('Destroy')
        layout.addWidget(self.clear_button)
        self.clear_button.clicked.connect(self.toggle_clear_mode)

        self.rectangle_drawer = None
        self.crop_add = None

        self.setCentralWidget(self.central_widget)  # Setting central widget

        widget.addWidget(self)

        self.rectangle_drawer_button.clicked.connect(self.showRectangleDrawer)
        self.crop_add_button.clicked.connect(self.call_crop_add)

    def call_crop_add(self):
        print("add crop button clicked")
        if not self.crop_add:
            self.crop_add = CropAdd()
        self.crop_add.setCursor(QCursor(Qt.CrossCursor))
        self.crop_add.show()
        self.crop_add.setCursor(QCursor(self.crop_add.cursor_pixmap))

    def toggle_clear_mode(self):
        if not self.crop_add:
            self.crop_add = CropAdd()
        # Toggle the clear mode of the crop add widget
        self.crop_add.set_clear_mode(True)
        self.crop_add.set_create_mode(False)
        
        
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
    sys.exit(app.exec_())
    
    self.clear_crops_button = QPushButton('Clear Crops')
        clear_crops_button.clicked.connect(lambda: widget.rectangles.clear() or widget.update())
        layout.addWidget(self.clear_crops_button)'''