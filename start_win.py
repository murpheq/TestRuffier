from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from instr import *
from second_win import TestWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setWindowIcon(QIcon('images/heart.ico'))

        self.label = QLabel(self)
        self.pixmap = QPixmap('images/bg.png')
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()

        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(fontTitle)
        self.hello_text.setStyleSheet('font-size: 36px')

        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(fontText)
        self.instruction.setStyleSheet('font-size: 24px')

        self.next_btn = QPushButton(txt_next)
        self.next_btn.setFont(fontBtn)
        self.next_btn.setObjectName('next_btn')
        self.next_btn.setStyleSheet(next_btn_StyleSheet)
        self.next_btn.setFixedWidth(170)
        
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.next_btn, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)

    def connects(self):
        self.next_btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
main = MainWindow()
app.exec()
    