from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QStackedWidget
import PyQt5

class Ui_PageFirst(QMainWindow):    #Page1

    def mainMenu(self, widget):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        new_game_button = QPushButton('New Game')
        new_game_button.clicked.connect(lambda: self.changeToPage2(widget))

        layout.addWidget(new_game_button)
        layout.addWidget(QPushButton('Exit'))
        self.setCentralWidget(central_widget)
        widget.addWidget(self)

    def changeToPage2(self, widget):
        widget.setCurrentIndex(1)


        