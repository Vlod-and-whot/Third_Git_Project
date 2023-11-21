import sys
from math import sin, cos, pi
from random import randint as rd

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Супрематизм')
        self.setMouseTracking(True)
        self.create_button = QPushButton('Create', self)
        self.create_button.move(200, 500)
        self.create_button.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = rd(20, 100)
        self.qp.setBrush(QColor('''*[rd(0, 255) for i in range(3)]'''))
        self.coords_ = [rd(0, 1000), rd(0, 1000)]
        self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                            int(self.coords_[1] - R / 2),
                            R, R)

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if (event.button() == Qt.LeftButton):
            self.status = 1
        elif (event.button() == Qt.RightButton):
            self.status = 2
        self.drawf()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
            self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())