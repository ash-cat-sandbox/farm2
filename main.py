from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QStackedWidget
import sys
from first_scene import Ui_PageFirst
from second_scene import Ui_PageSecond
from rectangle_drawer import RectangleDrawer

   
def main():

    app = QApplication(sys.argv)
    widget = QStackedWidget()

    firstpage = Ui_PageFirst()
    firstpage.mainMenu(widget)
    widget.addWidget(firstpage)   # create an instance of the first page class and add it to stackedwidget

    secondpage = Ui_PageSecond()
    secondpage.setupUI(widget)
    widget.addWidget(secondpage)
      # setting the page that you want to load when application starts up. you can also use setCurrentIndex(int)
    ########
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
