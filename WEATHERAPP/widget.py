from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = YOUR_API_KEY  # Replace with your OpenWeatherMap API key


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 500, 200)  # Set window size

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.fetch_button = QPushButton("Get Weather")
        self.result_label = QLabel("Weather info will appear here")
        self.result_label.setAlignment(Qt.AlignCenter)

     # Add widgets to layout
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.fetch_button)
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)

    # Connect button click to fetch weather
        self.fetch_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city_name = self.city_input.text()
        if not city_name:
            self.result_label.setText("Please enter a city name.")
            return

        # Fetch weather data
        url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200: 
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                self.result_label.setText(f"🌡 Temperature: {temp:.0f}°C\nCondition: {weather}\n💧 Humidity: {humidity}% \n 💨 Windspeed: {wind_speed} m/s")
            else:
                self.result_label.setText(f"Error: {data['message']}")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")
            