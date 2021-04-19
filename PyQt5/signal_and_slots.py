from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip
from PyQt5 import QtGui
import sys
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
#constructor
    def __init__(self):
        super().__init__()

        self.tittle="Qt Button"
        self.left=100
        self.top=100
        self.width=480
        self.height=500
        self.setWindowIcon(QtGui.QIcon("mahdi.jpg"))

        self.set_button()
        self.init_ui()

#for initialize
    def init_ui(self):
        self.setWindowTitle(self.tittle)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
#for create a button
    def set_button(self):
        button = QPushButton("Close", self)
        button.move(200,300)
        button.setToolTip("just for exit")
        button.clicked.connect(self.close)

#for close program
    def close(self):
        QCoreApplication.instance().quit()




if __name__ == '__main__':
    App=QApplication(sys.argv)
    obj=Window()
    sys.exit(App.exec())
