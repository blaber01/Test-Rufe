from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.move(win_x, win_y)
        self.resize(win_width,win_height)
    def initUI(self):
        self.txt_in = QLabel(txt_index)
        self.workhe = QLabel(txt_workheart)
        self.f_line = QVBoxLayout()
        self.f_line.addWidget(self.txt_in, alignment = Qt.AlignCenter)
        self.f_line.addWidget(self.workhe, alignment = Qt.AlignCenter)
        self.setLayout(self.f_line)
