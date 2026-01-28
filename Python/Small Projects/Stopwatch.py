import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)

       
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("▶ Start", self)
        self.stop_button = QPushButton("⏸ Stop", self)
        self.reset_button = QPushButton("🔄 Reset", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')
        self.setGeometry(500, 200, 400, 300)

       
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

      
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
            }
            QLabel {
                font-size: 80px;
                font-family: 'Arial Black';
                background-color: #1e1e1e;
                color: #00eaff;
                padding: 20px;
                border-radius: 20px;
                text-align: center;
                border: 2px solid #00eaff;
            }
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                font-family: 'Arial';
                color: white;
                background-color: #292929;
                border-radius: 10px;
                padding: 10px;
                margin: 5px;
                border: 2px solid #00eaff;
            }
            QPushButton:hover {
                background-color: #00eaff;
                color: black;
            }
        """)

       
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00.00")

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StopWatch()
    ex.show()
    sys.exit(app.exec_())
