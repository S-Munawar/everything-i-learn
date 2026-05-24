# PyQt5 Line Edits (QLineEdit)
# - QLineEdit: A widget that allows the user to enter and edit a single line of plain text.
# - .text(): Retrieves the current string inputted by the user.
# - .setText(string): Programmatically sets the string inside the line edit.
# - .setPlaceholderText(string): Shows a greyed-out hint when the box is empty.
# - .setEchoMode(): Used to hide text (like passwords) using QLineEdit.Password.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Line Edits")
        self.setGeometry(100, 100, 400, 350)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # 1. Header Label
        self.header = QLabel("🔐 Login Portal", self)
        self.header.setFont(QFont("Arial", 18, QFont.Bold))
        self.header.setAlignment(Qt.AlignCenter)
        
        # 2. Username Input (QLineEdit)
        self.input_username = QLineEdit(self)
        self.input_username.setFont(QFont("Arial", 14))
        # The placeholder text disappears the moment the user starts typing
        self.input_username.setPlaceholderText("Enter your username...")
        # CSS styling to make the input box look modern
        self.input_username.setStyleSheet("padding: 8px; border: 2px solid #BDC3C7; border-radius: 4px;")
        
        # 3. Password Input (QLineEdit)
        self.input_password = QLineEdit(self)
        self.input_password.setFont(QFont("Arial", 14))
        self.input_password.setPlaceholderText("Enter your password...")
        self.input_password.setStyleSheet("padding: 8px; border: 2px solid #BDC3C7; border-radius: 4px;")
        
        # IMPORTANT: QLineEdit.Password changes characters to dots/asterisks for security!
        self.input_password.setEchoMode(QLineEdit.Password)
        
        # 4. Submit Button
        self.btn_submit = QPushButton("Login", self)
        self.btn_submit.setStyleSheet("""
            QPushButton { background-color: #8E44AD; color: white; padding: 12px; font-weight: bold; border-radius: 4px; }
            QPushButton:hover { background-color: #9B59B6; }
        """)
        self.btn_submit.clicked.connect(self.on_submit)
        
        # 5. Result Label (For error/success messages)
        self.lbl_result = QLabel("", self)
        self.lbl_result.setFont(QFont("Arial", 12, QFont.Bold))
        self.lbl_result.setAlignment(Qt.AlignCenter)
        
        # Add widgets to layout
        layout.addWidget(self.header)
        layout.addSpacing(20)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addSpacing(15)
        layout.addWidget(self.btn_submit)
        layout.addWidget(self.lbl_result)
        
        layout.addStretch()
        central_widget.setLayout(layout)

    # --- Slot ---
    def on_submit(self):
        # Retrieve the text from the QLineEdits using .text()
        # .strip() removes accidental leading/trailing whitespaces from the username
        username = self.input_username.text().strip()
        password = self.input_password.text()
        
        # Basic validation
        if not username or not password:
            self.lbl_result.setText("❌ Error: Both fields are required!")
            self.lbl_result.setStyleSheet("color: #E74C3C;") # Red
            return
            
        # Hardcoded authentication check for demonstration purposes
        if username.lower() == "admin" and password == "password123":
            self.lbl_result.setText("✅ Access Granted! Welcome, Admin.")
            self.lbl_result.setStyleSheet("color: #27AE60;") # Green
            
            # .clear() is a built-in method that wipes the text field
            self.input_username.clear()
            self.input_password.clear()
        else:
            self.lbl_result.setText("❌ Invalid Credentials. Try again.")
            self.lbl_result.setStyleSheet("color: #E74C3C;") # Red

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# .text()  - O(N) Time - Where N is the number of characters in the input string.
# .clear() - O(N) Time - Linear time to safely deallocate the character buffer.
