# PyQt5 Layout Managers
# - Layout Managers: Classes that automatically arrange child widgets within a parent widget to make optimal use of space. They make your UI responsive (adaptable to window resizing).
# - Absolute Positioning (.setGeometry): Hardcoding X/Y coordinates. Generally bad practice because it breaks when the window is resized or opened on different screens.
# - QVBoxLayout: Arranges widgets vertically, from top to bottom.
# - QHBoxLayout: Arranges widgets horizontally, from left to right.
# - QGridLayout: Arranges widgets in a 2D grid of rows and columns.

import sys

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                                 QLabel, QVBoxLayout, QHBoxLayout, QGridLayout)
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Layout Managers")
        self.setGeometry(100, 100, 500, 500)
        
        self.initUI()
        
    def initUI(self):
        # IMPORTANT RULE: To use layouts in a QMainWindow, we MUST create a central "dummy" widget first.
        # QMainWindow has its own complex internal layout, so we can't apply our custom layouts directly to it.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # --- Create some colorful dummy widgets to organize ---
        label1 = QLabel("1")
        label1.setStyleSheet("background-color: #E74C3C; font-size: 40px; font-weight: bold;")
        
        label2 = QLabel("2")
        label2.setStyleSheet("background-color: #3498DB; font-size: 40px; font-weight: bold;")
        
        label3 = QLabel("3")
        label3.setStyleSheet("background-color: #2ECC71; font-size: 40px; font-weight: bold;")
        
        label4 = QLabel("4")
        label4.setStyleSheet("background-color: #F1C40F; font-size: 40px; font-weight: bold;")
        
        label5 = QLabel("5")
        label5.setStyleSheet("background-color: #9B59B6; font-size: 40px; font-weight: bold;")

        # --- Example 1: Vertical Layout (QVBoxLayout) ---
        # Uncomment this block to test the vertical layout
        """
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        central_widget.setLayout(vbox) 
        """

        # --- Example 2: Horizontal Layout (QHBoxLayout) ---
        # Uncomment this block to test the horizontal layout
        """
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        central_widget.setLayout(hbox)
        """
        
        # --- Example 3: Grid Layout (QGridLayout) ---
        # We will use this one by default!
        grid = QGridLayout()
        
        # syntax: .addWidget(widget, row, column, rowSpan, columnSpan)
        grid.addWidget(label1, 0, 0) # Top Left (Row 0, Col 0)
        grid.addWidget(label2, 0, 1) # Top Right (Row 0, Col 1)
        grid.addWidget(label3, 1, 0) # Bottom Left (Row 1, Col 0)
        grid.addWidget(label4, 1, 1) # Bottom Right (Row 1, Col 1)
        
        # Let's make label 5 span across 2 columns at the bottom
        grid.addWidget(label5, 2, 0, 1, 2) # Row 2, Col 0. Spans 1 row vertically, spans 2 columns horizontally.
        
        # Apply the chosen layout to our central dummy widget
        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# Adding Widget (.addWidget)           - O(1) Time - Constant time to append a reference to the layout structure.
# Window Resize (Layout Recalculation) - O(N) Time - Where N is the number of widgets. The GUI engine must iterate through and recalculate sizes dynamically during a window resize event.
