import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(700,300,500,500)
        self.setWindowTitle('My Window')

        self.checkbox=QCheckBox("Press this CheckBox",self)
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("color:#121212; font-size:20px;  font-family: 'Roboto', Arial, sans-serif; ")
        self.checkbox.stateChanged.connect(self.onStateChanged)

    def onStateChanged(self,state):
        if state == Qt.Checked:
            print("CheckBox is checked")
            self.checkbox.setText("You Clicked This!")
        else:
            print("CheckBox is unchecked")
            self.checkbox.setText("Press this CheckBox")
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
