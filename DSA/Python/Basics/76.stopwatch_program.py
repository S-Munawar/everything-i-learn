# Stopwatch Program
# - QTimer = A class that provides repetitive and single-shot timers. We use it to trigger an update for the stopwatch.
# - State Management = Keeping track of variables (e.g., elapsed time and running state) to manage the state of the stopwatch across different functions.
# - addMSecs() = A method of QTime that returns a new QTime object containing a time later by a specified number of milliseconds.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
    from PyQt5.QtCore import Qt, QTimer, QTime
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 450, 250)
        
        # State variables to keep track of time and status
        self.time_elapsed = QTime(0, 0, 0, 0)
        self.is_running = False
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Global window background styling (Dark Mode)
        self.setStyleSheet("background-color: #2C3E50;")
        
        main_layout = QVBoxLayout()
        
        # --- 1. Create the Time Display Label ---
        self.time_label = QLabel("00:00:00.000", self)
        self.time_label.setAlignment(Qt.AlignCenter)
        
        # Style the label to look like a digital display
        self.time_label.setStyleSheet("""
            color: #ECF0F1; 
            font-size: 55px; 
            font-weight: bold; 
            font-family: 'Consolas', 'Courier New', monospace;
            border: 2px solid #34495E;
            border-radius: 10px;
            padding: 10px;
            background-color: #1A252F;
            margin-bottom: 20px;
        """)
        
        main_layout.addWidget(self.time_label)
        
        # --- 2. Create the Buttons (Start, Stop, Reset) ---
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Start", self)
        self.stop_btn = QPushButton("Stop", self)
        self.reset_btn = QPushButton("Reset", self)
        
        # Premium CSS styling for buttons
        btn_style = """
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1F618D;
            }
        """
        
        # Apply special colors to specific buttons
        stop_btn_style = btn_style.replace("#3498DB", "#E74C3C").replace("#2980B9", "#C0392B").replace("#1F618D", "#922B21")
        reset_btn_style = btn_style.replace("#3498DB", "#95A5A6").replace("#2980B9", "#7F8C8D").replace("#1F618D", "#616A6B")
        
        self.start_btn.setStyleSheet(btn_style)
        self.stop_btn.setStyleSheet(stop_btn_style)
        self.reset_btn.setStyleSheet(reset_btn_style)
        
        # Connect buttons to their respective slot functions
        self.start_btn.clicked.connect(self.start_stopwatch)
        self.stop_btn.clicked.connect(self.stop_stopwatch)
        self.reset_btn.clicked.connect(self.reset_stopwatch)
        
        # Add buttons to the horizontal layout
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)
        button_layout.addWidget(self.reset_btn)
        
        # Add the horizontal layout to the main vertical layout
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)
        
        # --- 3. Setup QTimer ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
    def start_stopwatch(self):
        # Only start if it's not already running
        if not self.is_running:
            # 10 ms interval provides a smooth update for the milliseconds section
            self.timer.start(10)
            self.is_running = True
            
    def stop_stopwatch(self):
        # Only stop if it is currently running
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            
    def reset_stopwatch(self):
        # Stop the timer and reset the state and display
        self.timer.stop()
        self.is_running = False
        
        # Reset the QTime object to zero
        self.time_elapsed = QTime(0, 0, 0, 0)
        
        # Reset the label explicitly
        self.time_label.setText("00:00:00.000")
        
    def update_time(self):
        # Add 10 milliseconds to our time tracking object (since our timer ticks every 10ms)
        self.time_elapsed = self.time_elapsed.addMSecs(10)
        
        # Format the time (hh:mm:ss.zzz)
        # 'zzz' stands for milliseconds with leading zeroes
        time_text = self.time_elapsed.toString("hh:mm:ss.zzz")
        
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
# QTimer ticks      - O(1) Time - The update_time function executes constant work per timer interval.
# addMSecs()        - O(1) Time - QTime method that efficiently computes and returns a shifted time object.
# Layout Management - O(1) Time - Managing and rendering a fixed set of buttons is a constant time operation.
