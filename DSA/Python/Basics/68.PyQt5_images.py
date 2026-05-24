# PyQt5 Images
# - QPixmap: The primary class used to handle image rendering in PyQt5. 
# - It supports a wide variety of formats including PNG, JPEG, BMP, and GIF.
# - setScaledContents(True): A crucial method used on the QLabel. It forces the image to scale (stretch or shrink) to perfectly fit the label's dimensions.

import sys
import os
import urllib.request # Used to download a sample image for the lesson

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Basic window configuration
        self.setWindowTitle("PyQt5 Image Viewer")
        self.setGeometry(100, 100, 500, 500) # x, y, width, height
        
        self.initUI()
        
    def initUI(self):
        # --- 1. Download a Sample Image (For testing) ---
        # We need an image to display! Let's dynamically download the Python logo if it doesn't exist.
        image_filename = "python_logo_sample.png"
        
        if not os.path.exists(image_filename):
            print(f"📥 Downloading sample image '{image_filename}'...")
            url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
            # Fetches the image from the URL and saves it to the filename
            try:
                urllib.request.urlretrieve(url, image_filename)
            except Exception as e:
                print(f"⚠️ Failed to download sample image: {e}")
                return

        # --- 2. Create the Container Label ---
        # The label acts as the picture frame for our image
        image_label = QLabel(self)
        
        # Set the size and position of the frame
        image_label.setGeometry(50, 50, 400, 400)
        
        # Add a border so we can see the exact boundaries of the label
        image_label.setStyleSheet("border: 2px dashed #3498DB; padding: 10px;")
        
        # --- 3. Load the Image (QPixmap) ---
        # Instantiate a QPixmap object by passing the file path
        pixmap = QPixmap(image_filename)
        
        # Insert the pixmap (image) into the label
        image_label.setPixmap(pixmap)
        
        # --- 4. Scale the Image ---
        # By default, an image might be massive and overflow, or tiny and not fill the label.
        # This tells the image to stretch/shrink to fill the entire 400x400 geometry of the label.
        image_label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# QPixmap("file.png")   - O(N) Time - Where N is the size of the image file in bytes being loaded into RAM.
# setScaledContents()   - O(1) Time - Sets a configuration flag. The actual scaling algorithm runs during GUI rendering.
