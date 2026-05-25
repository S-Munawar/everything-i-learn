# Digital Clock Program
# - QTimer = A class that provides repetitive and single-shot timers. We use it to trigger an update function every second.
# - QTime = A class that provides clock time functions. We use it to retrieve the current system time.
# - toString() = A method of QTime used to format the time object into a readable string (e.g., 'hh:mm:ss AP').

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
    from PyQt5.QtCore import Qt, QTimer, QTime
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 450, 200)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Global window background styling (Cyberpunk/Retro digital look)
        self.setStyleSheet("background-color: #111111;")
        
        layout = QVBoxLayout()
        
        # --- 1. Create the Clock Label ---
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        
        # Style the label to look like a digital clock
        self.time_label.setStyleSheet("""
            color: #00FFCC; 
            font-size: 65px; 
            font-weight: bold; 
            font-family: 'Consolas', 'Courier New', monospace;
            border: 2px solid #00FFCC;
            border-radius: 10px;
            padding: 10px;
            background-color: #0A0A0A;
        """)
        
        layout.addWidget(self.time_label)
        central_widget.setLayout(layout)
        
        # --- 2. Setup QTimer ---
        # QTimer triggers a specific function (slot) at regular intervals.
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
        # Start the timer with an interval of 1000 milliseconds (1 second)
        self.timer.start(1000)
        
        # Call it once immediately so the clock doesn't start empty/blank for the first second
        self.update_time()
        
    def update_time(self):
        # --- 3. Update the Time ---
        # Get the current system time
        current_time = QTime.currentTime()
        
        # Format the time (hh:mm:ss AP -> 02:45:30 PM)
        # 'hh' = 12-hour format with leading zero
        # 'HH' = 24-hour format with leading zero
        # 'mm' = minutes with leading zero
        # 'ss' = seconds with leading zero
        # 'AP' = AM/PM
        time_text = current_time.toString("hh:mm:ss AP")
        
        # Update the label text
        self.time_label.setText(time_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# QTimer start      - O(1) Time - Initializing and starting the timer is a constant time operation.
# QTime currentTime - O(1) Time - Retrieving the system time is an O(1) OS-level call.
# Label Update      - O(1) Time - Updating the text of the QLabel happens in constant time.
