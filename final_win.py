from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *

class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp=exp
        self.initUI()
        self.set_appear()
        self.show()
    def results(self):
        self.index = (4 * (int(self.exp.test1_result)+ int(self.exp.test2_result)+ int(self.exp.test3_result)) - 200)/ 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return (txt_workheart + txt_res1)
            elif self.index >= 11 and self.index <= 14.9:
                return (txt_workheart + txt_res2)
            elif self.index >= 6 and self.index <= 10.9:
                return (txt_workheart + txt_res3)
            elif self.index >= 0.5 and self.index <= 5.9:
                return (txt_workheart + txt_res4)
            else:
                return (txt_workheart+ txt_res5)
        elif self.exp.age >= 13 and self.exp.age <= 14:
            if self.index >= 16.5:
                return (txt_workheart + txt_res1)
            elif self.index >= 12.5 and self.index <= 16.4:
                return (txt_workheart + txt_res2)
            elif self.index >= 7.5 and self.index <= 12.4:
                return (txt_workheart + txt_res3)
            elif self.index >= 2 and self.index <= 7.4:
                return (txt_workheart + txt_res4)
            else:
                return (txt_workheart+ txt_res5)
        elif self.exp.age >= 11 and self.exp.age <= 12:
            if self.index >= 18:
                return (txt_workheart + txt_res1)
            elif self.index >= 14 and self.index <= 17.9:
                return (txt_workheart + txt_res2)
            elif self.index >= 9 and self.index <= 13.9:
                return (txt_workheart + txt_res3)
            elif self.index >= 3.5 and self.index <= 8.9:
                return (txt_workheart + txt_res4)
            else:
                return (txt_workheart+ txt9es5)
        elif self.exp.age >= 13 and self.exp.age <= 10:
            if self.index >= 19.5:
                return (txt_workheart + txt_res1)
            elif self.index >= 15.5 and self.index <= 19.4:
                return (txt_workheart + txt_res2)
            elif self.index >= 10.5 and self.index <= 15.4:
                return (txt_workheart + txt_res3)
            elif self.index >= 5 and self.index <= 10.4:
                return (txt_workheart + txt_res4)
            else:
                return (txt_workheart+ txt_res5)
        elif self.exp.age >= 7 and self.exp.age <= 8:
            if self.index >= 21:
                return (txt_workheart + txt_res1)
            elif self.index >= 17 and self.index <= 20.9:
                return (txt_workheart + txt_res2)
            elif self.index >= 12 and self.index <= 16.9:
                return (txt_workheart + txt_res3)
            elif self.index >= 6.5 and self.index <= 11.9:
                return (txt_workheart + txt_res4)
            else:
                return (txt_workheart+ txt_res5)
    def initUI(self): 
       self.v_line = QVBoxLayout()
       self.score_text = QLabel(self.results())
       self.bye_text = QLabel(bye_text)
       self.v_line.addWidget(self.score_text, alignment= Qt.AlignCenter)
       self.v_line.addWidget(self.bye_text, alignment= Qt.AlignCenter)
       self.setLayout(self.v_line)
    def set_appear(self): 
        self.setWindowTitle(txt_title3)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
