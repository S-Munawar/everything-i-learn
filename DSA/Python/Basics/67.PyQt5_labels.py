# PyQt5 Labels (QLabel)
# - QLabel: A highly customizable widget used to display non-editable text or an image.
# - Styling: You can modify a label's font, alignment, and even apply CSS-like stylesheets.
# - QPixmap: An object designed to handle off-screen image representations. Used to insert images into QLabels.

import sys

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
    from PyQt5.QtGui import QFont, QPixmap
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window properties
        self.setWindowTitle("PyQt5 Labels & Styling Masterclass")
        self.setGeometry(100, 100, 600, 400) # x, y, width, height
        
        # We generally separate UI initialization into its own method to keep code clean
        self.initUI()
        
    def initUI(self):
        # --- 1. Basic Text Label ---
        # The 'self' parameter attaches the label to this specific MainWindow
        label_text = QLabel("Hello, I am a styled label!", self)
        
        # --- 2. Customizing the Font ---
        # QFont(family, pointSize, weight, italic)
        custom_font = QFont("Helvetica", 20, QFont.Bold, True)
        label_text.setFont(custom_font)
        
        # --- 3. Alignment ---
        # Options include: Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter, Qt.AlignTop, Qt.AlignBottom
        # You can combine them using the bitwise OR operator (|)
        label_text.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        
        # --- 4. Styling with CSS (StyleSheets) ---
        # PyQt5 allows you to style widgets using standard CSS syntax!
        label_text.setStyleSheet("""
            color: #2E86C1;
            background-color: #EAEDED;
            border: 3px solid #1A5276;
            border-radius: 10px;
            padding: 10px;
        """)
        
        # Manually set the geometry/position for the text label
        # .setGeometry(x, y, width, height)
        label_text.setGeometry(50, 30, 500, 80)
        
        
        # --- 5. Image Label (QPixmap) ---
        label_image = QLabel(self)
        label_image.setGeometry(200, 150, 200, 200) 
        
        # To display an actual image, you would use QPixmap like this:
        # pixmap = QPixmap("profile.jpg")
        # label_image.setPixmap(pixmap)
        # label_image.setScaledContents(True) # Scales the image to fit the label bounds
        
        # Since we don't have an image file here, we will style the label to look like a placeholder!
        label_image.setStyleSheet("""
            background-color: #E67E22; 
            border: 5px solid #D35400;
            border-radius: 100px; /* Makes a square label into a perfect circle */
            color: white;
        """)
        
        # Give the placeholder some text
        label_image.setText("🖼️\nImage Placeholder")
        label_image.setAlignment(Qt.AlignCenter)
        label_image.setFont(QFont("Arial", 12, QFont.Bold))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Label Creation      - O(1) Time - Constant time to instantiate the QLabel object in memory.
# Applying Stylesheet - O(1) Time - Constant time relative to the GUI engine parsing CSS text.
