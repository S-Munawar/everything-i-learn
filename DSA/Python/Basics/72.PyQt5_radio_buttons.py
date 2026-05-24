# PyQt5 Radio Buttons (QRadioButton)
# - QRadioButton: An option button that can be switched on (checked) or off (unchecked).
# - Mutually Exclusive: Unlike checkboxes, radio buttons belonging to the same parent are mutually exclusive by default (checking one unchecks all others).
# - QButtonGroup: Used to logically group radio buttons together. Essential if you need multiple, distinct sets of choices on the same window.

import sys

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton, QLabel, 
                                 QVBoxLayout, QWidget, QPushButton, QButtonGroup)
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt
except ImportError:
    print("❌ PyQt5 is not installed. Please run 'pip install PyQt5' in your environment.")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Radio Buttons")
        self.setGeometry(100, 100, 500, 450)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        
        # --- 1. First Group: Payment Method ---
        self.lbl_payment = QLabel("Select Payment Method:", self)
        self.lbl_payment.setFont(QFont("Arial", 14, QFont.Bold))
        
        # Create Radio Buttons
        self.radio_visa = QRadioButton("Visa", self)
        self.radio_mastercard = QRadioButton("MasterCard", self)
        self.radio_paypal = QRadioButton("PayPal", self)
        
        # Set a default selection
        self.radio_visa.setChecked(True)
        
        # Logically group the payment radio buttons using QButtonGroup.
        # This isolates them so they don't uncheck the shipping buttons below!
        self.payment_group = QButtonGroup(self)
        self.payment_group.addButton(self.radio_visa)
        self.payment_group.addButton(self.radio_mastercard)
        self.payment_group.addButton(self.radio_paypal)
        
        # --- 2. Second Group: Shipping Speed ---
        self.lbl_shipping = QLabel("\nSelect Shipping Speed:", self)
        self.lbl_shipping.setFont(QFont("Arial", 14, QFont.Bold))
        
        self.radio_standard = QRadioButton("Standard (3-5 days)", self)
        self.radio_express = QRadioButton("Express (1-2 days)", self)
        
        self.radio_standard.setChecked(True)
        
        # Logically group the shipping buttons separately
        self.shipping_group = QButtonGroup(self)
        self.shipping_group.addButton(self.radio_standard)
        self.shipping_group.addButton(self.radio_express)
        
        # --- 3. Toggled Signal Example ---
        # Radio buttons emit a 'toggled' signal when their state flips.
        self.radio_paypal.toggled.connect(self.on_paypal_toggled)
        
        # --- 4. Submit Button ---
        self.btn_checkout = QPushButton("Checkout Now", self)
        self.btn_checkout.setStyleSheet("background-color: #3498DB; color: white; padding: 12px; font-weight: bold; font-size: 14px; border-radius: 5px;")
        self.btn_checkout.clicked.connect(self.on_checkout)
        
        # --- 5. Result Label ---
        self.lbl_result = QLabel("", self)
        self.lbl_result.setFont(QFont("Arial", 12))
        
        # --- Add everything to the vertical layout ---
        main_layout.addWidget(self.lbl_payment)
        main_layout.addWidget(self.radio_visa)
        main_layout.addWidget(self.radio_mastercard)
        main_layout.addWidget(self.radio_paypal)
        
        main_layout.addWidget(self.lbl_shipping)
        main_layout.addWidget(self.radio_standard)
        main_layout.addWidget(self.radio_express)
        
        main_layout.addSpacing(25)
        main_layout.addWidget(self.btn_checkout)
        main_layout.addWidget(self.lbl_result)
        
        # Push everything to the top
        main_layout.addStretch()
        central_widget.setLayout(main_layout)

    # --- Slots ---
    def on_paypal_toggled(self):
        # This slot fires every time PayPal is checked OR unchecked
        radio = self.sender() # Get the specific button that triggered the signal
        if radio.isChecked():
            print("💳 PayPal selected! Get ready to redirect...")
        else:
            print("💳 PayPal deselected.")
            
    def on_checkout(self):
        # We can easily loop through a QButtonGroup to find which button is currently checked!
        payment_method = ""
        for button in self.payment_group.buttons():
            if button.isChecked():
                payment_method = button.text()
                break
                
        shipping_speed = ""
        for button in self.shipping_group.buttons():
            if button.isChecked():
                shipping_speed = button.text()
                break
                
        # Update the UI
        result_text = f"<b>✅ Order Summary:</b><br><br>- Paid via: <i>{payment_method}</i><br>- Shipping: <i>{shipping_speed}</i>"
        self.lbl_result.setText(result_text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# .isChecked()                   - O(1) Time - Constant time retrieval of boolean state.
# Iterate through QButtonGroup   - O(K) Time - Where K is the number of buttons in the group (typically small constant).
