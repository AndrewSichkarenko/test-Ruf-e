from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setObjectName("hello")
        self.instruction = QLabel(txt_instruction)
        self.instruction.setObjectName("instruction")
        self.btn_next = QPushButton(txt_next, self)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw= TestWin()
        self.hide()
    def connects(self): 
        self.btn_next.clicked.connect(self.next_click)
app = QApplication([])
mw = MainWin()
style = '''
    QWidget{
        background-color:#FFEBCD;
            font-size: 20px;
    }
    QLabel#instruction {
        width: 600px;
        text-align: center;
    }
    QLabel#hello {
        font-size: 30px
    }
    QPushButton {
        border: 2px solid black;
        border-radius: 4px;
        background: white;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-right : 10px;
        padding-left : 10px;
        font-weight: 500;
    }
'''
app.setStyleSheet(style)
app.exec_()
