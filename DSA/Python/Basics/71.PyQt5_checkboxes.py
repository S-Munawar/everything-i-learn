# PyQt5 Checkboxes (QCheckBox)
# - QCheckBox: A widget that provides an option the user can toggle on (checked) or off (unchecked).
# - It is typically used for options that are independent of each other (unlike Radio Buttons).
# - .isChecked(): Returns True if the box is currently checked, and False if it isn't.
# - stateChanged: A signal emitted automatically whenever the checkbox is toggled.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget, QPushButton
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Checkboxes")
        self.setGeometry(100, 100, 400, 350)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # 1. Header Label
        self.label = QLabel("Select your preferences:", self)
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        
        # 2. Create Checkboxes (QCheckBox)
        self.checkbox_food = QCheckBox("I like Pizza 🍕", self)
        self.checkbox_food.setFont(QFont("Arial", 14))
        
        self.checkbox_code = QCheckBox("I like Python 🐍", self)
        self.checkbox_code.setFont(QFont("Arial", 14))
        
        # .setChecked(True) can be used to make a box checked by default on launch
        self.checkbox_code.setChecked(True) 
        
        # 3. Create a Submit Button
        self.button = QPushButton("Submit Preferences", self)
        self.button.setFont(QFont("Arial", 12, QFont.Bold))
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #27AE60; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #2ECC71; }
        """)
        
        # 4. Result Label
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setStyleSheet("color: #2C3E50;") 
        
        # 5. Connect Signals
        # stateChanged signal is emitted whenever a box is checked/unchecked
        # It automatically passes the 'state' integer to the slot function
        self.checkbox_food.stateChanged.connect(self.on_checkbox_toggle)
        self.checkbox_code.stateChanged.connect(self.on_checkbox_toggle)
        
        # Connect the button click to our submit logic
        self.button.clicked.connect(self.on_submit)
        
        # 6. Add widgets to the vertical layout
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox_food)
        layout.addWidget(self.checkbox_code)
        
        # Add some spacing before the button
        layout.addSpacing(20) 
        
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        
        # Push everything to the top of the window instead of centering vertically
        layout.addStretch()
        
        central_widget.setLayout(layout)

    # --- Slot for stateChanged ---
    # The 'state' parameter is passed automatically by PyQt5
    # Qt.Checked equals 2, Qt.Unchecked equals 0
    def on_checkbox_toggle(self, state):
        sender = self.sender() # Identifies WHICH checkbox triggered the signal
        if state == Qt.Checked:
            print(f"[{sender.text()}] was checked!")
        else:
            print(f"[{sender.text()}] was unchecked!")

    # --- Slot for Button Click ---
    def on_submit(self):
        # We manually check the boolean state of the checkboxes using .isChecked()
        food_pref = self.checkbox_food.isChecked()
        code_pref = self.checkbox_code.isChecked()
        
        result_text = "<b>Your Profile:</b><br>"
        
        # Build the result string dynamically based on the booleans
        if food_pref:
            result_text += "- You love Pizza.<br>"
        else:
            result_text += "- You don't like Pizza?! 😱<br>"
            
        if code_pref:
            result_text += "- You are a Python master."
        else:
            result_text += "- You prefer another programming language."
            
        # We can render HTML directly inside QLabels!
        self.result_label.setText(result_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Checkbox Instantiation - O(1) Time - Constant time to build the widget.
# stateChanged Signal    - O(1) Time - Emitted instantly upon user interaction.
# .isChecked()           - O(1) Time - Constant time retrieval of boolean state.
