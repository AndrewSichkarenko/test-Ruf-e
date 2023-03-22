from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title3)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
       self.v_line = QVBoxLayout()
       self.score_text = QLabel(score_text)
       self.bye_text = QLabel(bye_text)
       self.v_line.addWidget(self.score_text, alingment= Qt.AlignCenter)
       self.v_line.addWidget(self.bye_text, alingment= Qt.AlignCenter)
       self.setLayout(self.v_line)
app = QApplication([])
app.exec_()
