import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)

        label = QLabel(self)
        label.setGeometry(0,0,250,350)
        pixmap= QPixmap(r"Learning\Bavan.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
def main():
    app=QApplication(sys.argv) 
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main() 