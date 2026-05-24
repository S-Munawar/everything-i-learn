# PyQt5 GUI Introduction
# - GUI (Graphical User Interface): A visual way for users to interact with a program using windows, buttons, and text fields.
# - PyQt5: A comprehensive set of Python bindings for the Qt framework. It allows you to create robust desktop applications.
#   * NOTE: You must install it first by running: pip install PyQt5
# - QApplication: The main application object that manages the GUI control flow and settings.
# - QMainWindow / QWidget: The base classes for user interface objects (e.g., the window itself).

import sys

# We use a try-except block here because PyQt5 is a 3rd-party library that might not be installed.
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed.")
    print("👉 Please run 'pip install PyQt5' in your terminal (or inside your .venv) to run this script.")
    sys.exit()

print("--- 🖥️ Introduction to PyQt5 GUI 🖥️ ---")
print("Launching GUI Window... (Check your taskbar if it doesn't pop up immediately!)")

class MainWindow(QMainWindow):
    def __init__(self):
        # super().__init__() initializes the QMainWindow parent class
        super().__init__()
        
        # --- 1. Window Configuration ---
        # Set the title at the top of the window
        self.setWindowTitle("My First PyQt5 GUI")
        
        # Set the window size and position on the screen
        # .setGeometry(x_position, y_position, width, height)
        self.setGeometry(100, 100, 500, 300)
        
        # --- 2. Adding Widgets (Components) ---
        # Create a label (text) and attach it to 'self' (this window)
        label = QLabel("Hello, PyQt5!", self)
        
        # Customize the label's font
        font = QFont("Arial", 24, QFont.Bold)
        label.setFont(font)
        
        # Align the text to the center of the window
        label.setAlignment(Qt.AlignCenter)
        
        # Set the label as the central widget so it expands to fill the window
        self.setCentralWidget(label)

def main():
    # 1. Create the application instance (sys.argv allows passing command-line arguments to the app)
    app = QApplication(sys.argv)
    
    # 2. Create an instance of our custom window class
    window = MainWindow()
    
    # 3. Show the window on the screen
    window.show()
    
    # 4. Start the application's main event loop.
    # The event loop listens for clicks, key presses, etc.
    # sys.exit() ensures a clean process exit when the window is closed.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# GUI Initialization - O(1) Time - Constant time to set up and render the initial window components.
# Event Loop (app.exec_()) - O(1) Time per event - Runs infinitely, processing user interactions as they occur.
