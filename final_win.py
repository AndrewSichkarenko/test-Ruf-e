from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *

class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self): 
        self.setWindowTitle(txt_title3)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self): 
       self.v_line = QVBoxLayout()
       self.score_text = QLabel(score_text)
       self.bye_text = QLabel(bye_text)
       self.v_line.addWidget(self.score_text, alignment= Qt.AlignCenter)
       self.v_line.addWidget(self.bye_text, alignment= Qt.AlignCenter)
       self.setLayout(self.v_line)
    def results(self):
        self.index = (4 * (int(self.test1_result)+ int(self.test2_result)+ int(self.test3_result)) - 200)/ 10
        if self.age >= 15:
            if self.index >= 15:
                print(txt_workheart + txt_res1)
            elif self.index >= 11 and self.index <= 14.9:
                print(txt_workheart + txt_res2)
            elif self.index >= 6 and self.index <= 10.9:
                print(txt_workheart + txt_res3)
            elif self.index >= 0.5 and self.index <= 5.9:
                print(txt_workheart + txt_res4)
            else:
                print(txt_workheart+ txt_res5)
        elif self.age >= 13 and self.age <= 14:
            if self.index >= 16.5:
                print(txt_workheart + txt_res1)
            elif self.index >= 12.5 and self.index <= 16.4:
                print(txt_workheart + txt_res2)
            elif self.index >= 7.5 and self.index <= 12.4:
                print(txt_workheart + txt_res3)
            elif self.index >= 2 and self.index <= 7.4:
                print(txt_workheart + txt_res4)
            else:
                print(txt_workheart+ txt_res5)
        elif self.age >= 11 and self.age <= 12:
            if self.index >= 18:
                print(txt_workheart + txt_res1)
            elif self.index >= 14 and self.index <= 17.9:
                print(txt_workheart + txt_res2)
            elif self.index >= 9 and self.index <= 13.9:
                print(txt_workheart + txt_res3)
            elif self.index >= 3.5 and self.index <= 8.9:
                print(txt_workheart + txt_res4)
            else:
                print(txt_workheart+ txt9es5)
        elif self.age >= 13 and self.age <= 10:
            if self.index >= 19.5:
                print(txt_workheart + txt_res1)
            elif self.index >= 15.5 and self.index <= 19.4:
                print(txt_workheart + txt_res2)
            elif self.index >= 10.5 and self.index <= 15.4:
                print(txt_workheart + txt_res3)
            elif self.index >= 5 and self.index <= 10.4:
                print(txt_workheart + txt_res4)
            else:
                print(txt_workheart+ txt_res5)
        elif self.age >= 7 and self.age <= 8:
            if self.index >= 21:
                print(txt_workheart + txt_res1)
            elif self.index >= 17 and self.index <= 20.9:
                print(txt_workheart + txt_res2)
            elif self.index >= 12 and self.index <= 16.9:
                print(txt_workheart + txt_res3)
            elif self.index >= 6.5 and self.index <= 11.9:
                print(txt_workheart + txt_res4)
            else:
                print(txt_workheart+ txt_res5)
