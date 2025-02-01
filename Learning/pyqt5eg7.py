import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QLineEdit,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700,300,500,500)

        self.line_edit=QLineEdit(self)
        self.button=QPushButton("Submit",self)
        self.label = QLabel("", self)

        self.line_edit.setPlaceholderText("Enter Your Name...")
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.label.setGeometry(10, 60, 300, 40)

        self.line_edit.setStyleSheet("font-size:20px;"
                                     "font-family:Arial")
        self.label.setStyleSheet("font-size:30px; font-family:Arial; color:blue") 
        self.button.setStyleSheet("font-size:20px")
        self.button.clicked.connect(self.on_click)

    def on_click(self):

        text=self.line_edit.text()
        self.label.setText(f"Hello {text}")
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
