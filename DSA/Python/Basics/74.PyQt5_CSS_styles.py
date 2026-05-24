# PyQt5 CSS Styles (StyleSheets)
# - setStyleSheet(): A method inherited by all QWidgets that allows you to style them using standard CSS (Cascading Style Sheets) syntax.
# - Global Styling: Instead of styling every single button manually, you can apply a master stylesheet to the main window, and it will cascade down to all children.
# - CSS Selectors: Just like web development, you can use selectors (e.g., 'QPushButton') to style all widgets of a class, or ID selectors (e.g., '#myButton') to style a specific object.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 CSS Styling Masterclass")
        self.setGeometry(100, 100, 450, 400)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        
        # --- 1. Global Window Styling (The "Theme") ---
        # By defining a massive CSS string and applying it to the QMainWindow,
        # we create a centralized theme that governs the look of every widget inside it.
        
        global_theme = """
            /* 1. Style the main window background (Dark Mode) */
            QMainWindow {
                background-color: #2C3E50;
            }
            
            /* 2. Style ALL Labels universally */
            QLabel {
                color: #ECF0F1;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 16px;
                font-weight: bold;
            }
            
            /* 3. Style ALL Buttons universally */
            QPushButton {
                background-color: #34495E;
                color: #ECF0F1;
                border: 2px solid #2980B9;
                border-radius: 8px;
                padding: 12px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            
            /* Hover effects for all buttons */
            QPushButton:hover {
                background-color: #2980B9;
                border: 2px solid #3498DB;
            }
            
            /* Pressed effects for all buttons */
            QPushButton:pressed {
                background-color: #1A5276;
            }
            
            /* 4. ID Selectors (#) target one specific widget using its ObjectName! */
            QPushButton#dangerBtn {
                background-color: #C0392B;
                border: 2px solid #E74C3C;
            }
            QPushButton#dangerBtn:hover {
                background-color: #E74C3C;
                border: 2px solid #F1948A;
            }
        """
        # Apply the master theme to the entire window
        self.setStyleSheet(global_theme)
        
        # --- 2. Building the UI ---
        lbl_title = QLabel("Welcome to the Dark Theme", self)
        lbl_title.setAlignment(Qt.AlignCenter)
        
        # Note: Local stylesheets OVERRIDE global stylesheets!
        lbl_title.setStyleSheet("font-size: 26px; color: #3498DB; margin-bottom: 20px;") 
        
        # These buttons will automatically inherit the global 'QPushButton' styling!
        btn_normal1 = QPushButton("Standard Action 1", self)
        btn_normal2 = QPushButton("Standard Action 2", self)
        
        # This button is special. We assign it an "ObjectName" so the CSS ID selector (#dangerBtn) can find it.
        btn_danger = QPushButton("Delete Everything", self)
        btn_danger.setObjectName("dangerBtn") 
        
        # --- Add to layout ---
        main_layout.addWidget(lbl_title)
        main_layout.addWidget(btn_normal1)
        main_layout.addWidget(btn_normal2)
        
        # Let's create a visual line separator using a styled QWidget
        separator = QWidget()
        separator.setFixedHeight(2)
        separator.setStyleSheet("background-color: #7F8C8D; margin: 15px 0px;")
        main_layout.addWidget(separator)
        
        main_layout.addWidget(btn_danger)
        
        main_layout.addStretch()
        central_widget.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Stylesheet Parsing - O(N) Time - N is the character length of the CSS string. Parsed once upon initialization.
# Style Cascade      - O(K) Time - K is the number of child widgets in the tree that the styles must be applied to.
