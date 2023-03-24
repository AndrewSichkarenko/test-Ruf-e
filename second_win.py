from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *
from final_win import *
class TestWin(QWidget):
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
        self.hor_line = QHBoxLayout()
        self.v_line = QVBoxLayout()
        self.v2_line = QVBoxLayout()

        self.hintname = QLabel(txt_hintname)
        self.hintage = QLabel(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.timer = QLabel('00:00:00')
        self.starttest1 = QPushButton(txt_starttest1)
        self.starttest2 = QPushButton(txt_starttest2)
        self.starttest3 = QPushButton(txt_starttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.name = QLineEdit('П.І.Б.')
        self.age = QLineEdit('0')
        self.test1_result = QLineEdit('0')
        self.test2_result = QLineEdit('0')
        self.test3_result = QLineEdit('0')

        self.v_line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.starttest1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test1_result, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.starttest2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test2_result, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.starttest3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test3_result, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)
        self.v2_line.addWidget(self.timer, alignment = Qt.AlignRight)
        self.hor_line.addLayout(self.v_line)
        self.hor_line.addLayout(self.v2_line)
        self.setLayout(self.hor_line)
    def next_click(self):
        self.fw= FinalWin()
        self.hide()
    def connects(self): 
        self.sendresults.clicked.connect(self.next_click)
