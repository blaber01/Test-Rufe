from instr import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup
from final_win import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_width,win_height)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.txt_name1 = QLabel(txt_name)
        self.line_name = QLineEdit(txt_hintname)
        self.txt_age2 = QLabel(txt_age)
        self.line_age2 = QLineEdit(txt_hintage)

        self.txt_test3 = QLabel(txt_test1)
        self.line_test3 = QLineEdit(txt_hinttest1)
        self.txt_test4 = QLabel(txt_test2)
        self.line_test4 = QLineEdit(txt_hinttest2)
        self.txt_test5 = QLabel(txt_test3)
        self.line_test5 = QLineEdit(txt_hinttest3)

        self.button13 = QPushButton(txt_starttest1)
        self.button22 = QPushButton(txt_starttest2)
        self.button31 = QPushButton(txt_starttest3)
        self.next = QPushButton(txt_next)
        self.text_timer = QLabel()
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button13, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button22, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button31, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test5, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.next, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.next.clicked.connect(self.next_click)
        self.button13.clicked.connect(self.timer_test)
        self.button22.clicked.connect(self.timer_sits)
        self.button31.clicked.connect(self.timer_final)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age2.text(),self.line_test3.text(),self.line_test4.text(),self.line_test5.text())
        self.fw = FinalWin(self.exp)
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(255,0,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
