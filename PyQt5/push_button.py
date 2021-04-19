from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip
from PyQt5 import QtGui
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tittle="Qt Button"
        self.left=100
        self.top=100
        self.width=480
        self.height=500



        self.set_button()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle(self.tittle)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def set_button(self):
        button = QPushButton("click on me:)", self)
        button.move(200,200)
        button.setToolTip("Hi it's me")




if __name__ == '__main__':
    App=QApplication(sys.argv)
    obj=Window()
    sys.exit(App.exec())
