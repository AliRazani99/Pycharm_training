from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip,QMessageBox,QStatusBar
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tittle="PyQt5"
        self.left=100
        self.top=100
        self.width=480
        self.height=500
        self.setWindowIcon(QtGui.QIcon("mahdi.jpg"))




        self.set_button()
        self.init_ui()


    def init_ui(self):
        self.statusBar().showMessage("This is new status bar")
        self.setWindowTitle(self.tittle)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def set_button(self):
        first_button = QPushButton("first", self)
        first_button.move(200, 300)
        first_button.setToolTip("just for exit")
        first_button.clicked.connect(self.about_messages)

        second_button = QPushButton("second", self)
        second_button.move(200, 200)
        second_button.setToolTip("just for asking exit")
        second_button.clicked.connect(self.question_messages)

    def  about_messages(self):
        QMessageBox.about(self,"Mahdi","Hi my friends this is my new About button")



    def question_messages(self):
        message = QMessageBox.question(self, "Close Message", "Are you sure?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if message==QMessageBox.Yes:
            self.close()


    def quit(self):
        QCoreApplication.instance().quit()




if __name__ == '__main__':
    App=QApplication(sys.argv)
    obj=Window()
    sys.exit(App.exec())
