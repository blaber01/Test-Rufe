from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup
app = QApplication([])
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        #self.connects()
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
        self.timer = QLabel(txt_timer)
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
        self.r_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.next, alignment = Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click():
        self.hide(TestWin)

main_win = TestWin()
app.exec_()
