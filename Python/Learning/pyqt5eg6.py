import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Radio Button')
        
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("Master Card",self)
        self.radio4=QRadioButton("In-store",self)
        self.radio5=QRadioButton("Online",self)


        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
      

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)


        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio4.setGeometry(0,100,300,50)
        self.radio5.setGeometry(0,150,300,50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family:Arial;"
                           "padding: 10px"
                           "}")


        self.radio1.toggled.connect(self.toggled)
        self.radio2.toggled.connect(self.toggled)
        self.radio4.toggled.connect(self.toggled)
        self.radio5.toggled.connect(self.toggled)


    def toggled(self):
        radio_button=self.sender()
        if radio_button.isChecked():
            print(f"You Selected {radio_button.text()}")
        else:
            print("No radio button is selected")
   

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
