#Weather App 
import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt 


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter City Name: ",self)
        self.city_input=QLineEdit(self) 
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()


    def initUI(self):

        self.setWindowTitle("Weather App")

        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
    QWidget {
        background-color: #b2ceeb;
    }
    
    QLabel, QPushButton {
        font-family: 'Arial', sans-serif;
    }
    
    QLabel#city_label {
        font-size: 32px;
        font-weight: bold;
        color: #333333;
        padding: 10px;
    }
    
    QLineEdit#city_input {
        font-size: 24px;
        padding: 10px;
        margin-bottom: 20px;
        border: 2px solid #ddd;
        border-radius: 5px;
        background-color: #ffffff;
        color: #333333;
    }

    QPushButton#get_weather_button {
        font-size: 26px;
        font-weight: bold;
        color: white;
        background-color: #579ce6;
        border: none;
        border-radius: 8px;
        padding: 15px;
    }

    QPushButton#get_weather_button:hover {
        background-color: #579ce6;
    }

    QLabel#temperature_label {
        font-size: 80px;
        color: black;
        margin-top: 20px;
    }

    QLabel#emoji_label {
        font-size: 100px;
        font-family: 'Segoe UI Emoji', sans-serif;
        margin-top: 20px;
    }

    QLabel#description_label {
        font-size: 36px;
        color: black;
        margin-top: 20px;
    }

    QLabel#city_label, QLabel#temperature_label, QLabel#emoji_label, QLabel#description_label {
        text-align: center;
    }
""")




        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        api_key="7fc9e945a03d2dad3a1d52f0f296920a"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data['cod']==200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_err:

            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")
                case 404:
                    self.display_error("Not found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Server ERROR:\nPlease Try Again Later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid Response From Server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is Down")
                case 504:
                    self.display_error("Gateway Timeout!:\nNo Response From Server")
                case _:
                    self.display_error(f"An error occurred;\n{http_err}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck Your Internet COnnection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe Request is Timed Out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects Error:\nCheck The URL")

        except requests.exceptions.RequestException as req_err:
            self.display_error(f"An error occurred:\n{req_err}")




    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temp_k=data['main']['temp']
        temp_c=temp_k-273.15
        temp_f=(temp_k*9/5)-459.67
        weather_id=data['weather'][0]['id']
        weather_desc=data['weather'][0]['description']
        weather_desc=weather_desc.capitalize()
        
       
        self.temperature_label.setText(f"{temp_c:.0f}°C")
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.description_label.setText(weather_desc)

    @staticmethod
    def get_emoji(weather_id):
        if 200<=weather_id <= 230 :
            return "⛈️"
        elif 300<=weather_id <= 321 :
            return "🌦️"
        elif 500<=weather_id <= 531 :
            return "🌨️"
        elif 600<=weather_id <= 622:
            return "❄️"
        elif 701<=weather_id <= 741 :
            return "🌫️"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "💨"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"
        elif 801<=weather_id <= 804 :
            return "☁️"
        else:
            return 



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=WeatherApp()
    window.show()
    sys.exit(app.exec_())