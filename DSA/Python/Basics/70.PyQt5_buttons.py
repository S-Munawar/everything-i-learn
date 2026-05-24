# PyQt5 Buttons (QPushButton)
# - QPushButton: A widget that provides a standard, clickable command button.
# - Signals and Slots: The core mechanism PyQt5 uses for communication between objects.
#   * Signal: Emitted when an event occurs (e.g., a button is clicked, mouse is moved).
#   * Slot: A regular Python function that is called in response to a particular signal.
# - .clicked.connect(slot_function): Connects the button's internal "clicked" signal to a specified function.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Buttons & Signals")
        self.setGeometry(100, 100, 400, 300)
        
        # State tracking variable
        self.click_count = 0 
        
        self.initUI()
        
    def initUI(self):
        # 1. Central Widget and Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # 2. Information Label
        self.label = QLabel("Ready to click!", self)
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        
        # 3. Create the Button (QPushButton)
        self.button = QPushButton("Click Me!", self)
        self.button.setFont(QFont("Arial", 14, QFont.Bold))
        
        # We can use CSS pseudo-classes like :hover and :pressed to make the button interactive!
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 8px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1A5276;
            }
        """)
        
        # 4. Signals and Slots (The Brains of the Operation)
        # We connect the button's "clicked" signal to our custom "on_button_click" function.
        # CRITICAL RULE: Pass the reference to the function. Do NOT put parentheses at the end! 
        # (e.g., self.on_button_click, NOT self.on_button_click())
        self.button.clicked.connect(self.on_button_click)
        
        # 5. Add widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        central_widget.setLayout(layout)

    # --- This is our "Slot" function ---
    def on_button_click(self):
        # Update our internal state
        self.click_count += 1
        
        # Dynamically change the UI label text based on state
        if self.click_count == 1:
            self.label.setText("Button clicked 1 time. 🖱️")
        else:
            self.label.setText(f"Button clicked {self.click_count} times! 🔥")
            
        # Example of dynamically changing the button's state based on conditions
        if self.click_count >= 5:
            self.label.setText("🛑 Maximum Clicks Reached!")
            self.button.setText("Disabled")
            
            # Override the stylesheet to a dull gray
            self.button.setStyleSheet("""
                QPushButton {
                    background-color: #95A5A6; 
                    color: white; 
                    border-radius: 8px; 
                    padding: 15px;
                }
            """)
            
            # .setDisabled(True) completely deactivates the button so it can't be clicked anymore
            self.button.setDisabled(True) 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Button Instantiation - O(1) Time - Constant time to initialize the widget object.
# Signal Connection    - O(1) Time - Constant time to link the event listener.
# Slot Execution       - O(1) Time - Our slot simply executes basic variable incrementing and GUI string updates.
