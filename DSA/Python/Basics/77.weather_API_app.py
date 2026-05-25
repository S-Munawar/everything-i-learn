# Weather API App
# - Requests = A popular third-party Python library for making HTTP requests to external APIs.
# - API (Application Programming Interface) = A set of rules that allows one software application to talk to another.
# - JSON (JavaScript Object Notation) = A lightweight data-interchange format. We use it to parse the data returned by the API.

import sys
import requests

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather API Application")
        self.setGeometry(100, 100, 450, 550)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Clean background theme
        self.setStyleSheet("background-color: #34495E;")
        
        main_layout = QVBoxLayout()
        
        # --- 1. Title Label ---
        self.title_label = QLabel("Global Weather", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #ECF0F1; font-size: 34px; font-weight: bold; margin-bottom: 10px;")
        
        # --- 2. City Input Field ---
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter City Name (e.g. London, Tokyo)")
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_input.setStyleSheet("""
            QLineEdit {
                font-size: 20px;
                padding: 12px;
                border: 2px solid #2980B9;
                border-radius: 8px;
                background-color: #2C3E50;
                color: #ECF0F1;
            }
            QLineEdit:focus {
                border: 2px solid #3498DB;
            }
        """)
        
        # --- 3. Search Button ---
        self.search_btn = QPushButton("Get Weather", self)
        self.search_btn.setStyleSheet("""
            QPushButton {
                background-color: #27AE60;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 14px;
                font-size: 18px;
                font-weight: bold;
                margin-top: 10px;
                margin-bottom: 30px;
            }
            QPushButton:hover {
                background-color: #2ECC71;
            }
            QPushButton:pressed {
                background-color: #1E8449;
            }
        """)
        # Connect clicking the button and hitting "Enter" in the input field to the get_weather function
        self.search_btn.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)
        
        # --- 4. Result Labels ---
        self.temperature_label = QLabel("", self)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet("color: #F1C40F; font-size: 60px; font-weight: bold;")
        
        self.emoji_label = QLabel("", self)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setStyleSheet("font-size: 90px;")
        
        self.description_label = QLabel("", self)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("color: #BDC3C7; font-size: 26px; font-weight: bold;")
        
        # Add widgets to layout
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.city_input)
        main_layout.addWidget(self.search_btn)
        main_layout.addWidget(self.temperature_label)
        main_layout.addWidget(self.emoji_label)
        main_layout.addWidget(self.description_label)
        
        # Add stretch to push everything to the top and give breathing room
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        
    def get_weather(self):
        # ⚠️ NOTE: Replace this with your actual OpenWeatherMap API key!
        api_key = "YOUR_API_KEY_HERE"
        city = self.city_input.text().strip()
        
        if not city:
            self.display_error("Please enter a city name.")
            return
            
        # Standard OpenWeatherMap Endpoint (units=metric provides Celsius, use units=imperial for Fahrenheit)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            # Send HTTP GET request
            response = requests.get(url)
            
            # Check for HTTP errors (e.g. 401 Unauthorized, 404 Not Found)
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 401:
                self.display_error("Invalid API Key.\nPlease add your key in the code.")
            elif response.status_code == 404:
                self.display_error("City not found.\nTry another name.")
            else:
                self.display_error(f"HTTP Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            # Handle connection errors (e.g., no internet access)
            self.display_error("Connection Error.\nCheck your internet.")
            print(f"Exception: {e}")
            
    def display_error(self, message):
        self.temperature_label.setText("Error")
        self.temperature_label.setStyleSheet("color: #E74C3C; font-size: 40px; font-weight: bold;")
        self.emoji_label.setText("⚠️")
        self.description_label.setText(message)
        
    def display_weather(self, data):
        # Parse JSON data
        temp = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"].title()
        
        # Reset color back to standard yellow in case it was an error previously
        self.temperature_label.setStyleSheet("color: #F1C40F; font-size: 60px; font-weight: bold;")
        
        self.temperature_label.setText(f"{temp:.1f}°C")
        self.description_label.setText(description)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        
    def get_weather_emoji(self, weather_id):
        # OpenWeatherMap condition codes
        # 2xx: Thunderstorm, 3xx: Drizzle, 5xx: Rain, 6xx: Snow, 7xx: Atmosphere, 800: Clear, 80x: Clouds
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "🌡️"

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Network Request - O(1) Time - Requesting data is theoretically constant relative to local CPU time, though bound by network latency.
# JSON Parsing    - O(N) Time - N is the character length of the JSON string being parsed.
# UI Updates      - O(1) Time - Updating text and styles for QLabels is a constant time operation.
