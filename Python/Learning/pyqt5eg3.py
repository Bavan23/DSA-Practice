import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QVBoxLayout,QHBoxLayout,QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100,100,800,600)
        self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("Hi",self)
        label2=QLabel("Hello",self)
        label3=QLabel("Hola",self)
        label4=QLabel("Hey",self)

        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)


        label1.setStyleSheet("background-color:red;""font-size:150px")
        label2.setStyleSheet("background-color:blue;""font-size:150px")
        label3.setStyleSheet("background-color:green;""font-size:150px")
        label4.setStyleSheet("background-color:yellow;""font-size:150px")

        vbox=QGridLayout()

        vbox.addWidget(label1,0,0)
        vbox.addWidget(label2,0,1)
        vbox.addWidget(label3,1,0)
        vbox.addWidget(label4,1,1)

        central_widget.setLayout(vbox)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
