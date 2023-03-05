import PyQt5 as pyqt5
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QLineEdit ,QPlainTextEdit
from PyQt5 import uic
from CAH import CAH_algorithme ,string_to_list_of_sublist

class Classification(QMainWindow):
    def __init__(self):
        super(Classification , self).__init__()
        # load the UI
        uic.loadUi('Data Mining/weka_copy/main screen CAH.ui' , self)

        # locate the widgets
        self.text_input = self.findChild(QLineEdit , 'lineEdit')
        self.input_type = self.findChild(QLineEdit , 'lineEdit_2')
        self.button = self.findChild(QPushButton , 'pushButton')
        self.button.clicked.connect(self.button_pressed)
        self.text_output = self.findChild(QPlainTextEdit , 'plainTextEdit')

        # show the UI
        self.show()
    
    def button_pressed(self):
        self.text_output.setPlainText('')
        text_input = string_to_list_of_sublist(self.text_input.text())#type:ignore
        result = CAH_algorithme(text_input , int(self.input_type.text()))
        for index ,classification in enumerate(result):
            self.text_output.insertPlainText(f"{index} : {classification}\n")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    UI = Classification()
    app.exec_()