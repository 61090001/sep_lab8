import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Drawing_Alex(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.rabbit = QPixmap('image/spiderman.png')
        self.pickle = QPixmap('image/pickle.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(50, 50, 110, 150), self.pickle)
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Drawing_Alex()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())