from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox
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
        first_button = QPushButton("Close", self)
        first_button.move(200,300)
        first_button.setToolTip("just for exit")
        first_button.clicked.connect(self.close)

        second_button=QPushButton("Asking for close",self)
        second_button.move(200, 200)
        second_button.setToolTip("just for asking exit")
        second_button.clicked.connect(self.closeApp)



    def closeApp(self):
        reply = QMessageBox.question(self,"Close Message","Are you sure?",QMessageBox.Yes |QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

#for close program
    def close(self):
        QCoreApplication.instance().quit()




if __name__ == '__main__':
    App=QApplication(sys.argv)
    obj=Window()
    sys.exit(App.exec())
