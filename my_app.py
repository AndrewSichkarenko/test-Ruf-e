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
        self.instruction = QLabel(txt_instruction)
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
app.exec_()
