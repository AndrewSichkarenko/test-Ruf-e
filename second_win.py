from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QFont
from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1_result, test2_result, test3_result):
        self.age = age 
        self.test1_result = test1_result
        self.test2_result = test2_result
        self.test3_result = test3_result

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
        self.text_timer = QLabel('00:00:00')
        self.text_timer.setFont(QFont("monospaced", 36, QFont.Bold))
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
        self.v_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.starttest3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test2_result, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test3_result, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)
        self.v2_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.hor_line.addLayout(self.v_line)
        self.hor_line.addLayout(self.v2_line)
        self.setLayout(self.hor_line)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer2_test(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer3_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("monospaced", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        timer = self.text_timer
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("monospaced", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("monospaced", 36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.age.text()), int(self.test1_result.text()), int(self.test2_result.text()), int(self.test3_result.text()))
        self.fw= FinalWin(self.exp)

    def connects(self): 
        self.sendresults.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer2_test)
        self.starttest3.clicked.connect(self.timer3_test)
