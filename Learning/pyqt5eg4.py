import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(700,300,500,500)
        self.setWindowTitle('PyQt5')
        self.setWindowIcon(QIcon('Learning\Bavan.jpg'))

        self.label=QLabel("Hello",self)
        self.label.setFont(QFont("Tahoma",20))
        self.label.setStyleSheet("font-size:50px; background-color: black; color:white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50,50,200,100)

        self.button=QPushButton("Click Me",self)
        self.button.setGeometry(150,150,250,100)
        self.button.setStyleSheet("background-color: blue;""font-size:50px")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked")
        self.button.setStyleSheet("background-color: red;""font-size:30px")
        self.button.setText("You Clicked Me")
        self.label.setText("World!")
        self.label.setStyleSheet("font-size:30px; background-color: Green; color:white;")



def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
