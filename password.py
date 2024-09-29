import sys
import random
import string
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QSlider, QLineEdit, QHBoxLayout, QCheckBox, QFrame, QStyleFactory, QMessageBox
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Advanced Password Generator")
        self.setGeometry(200, 200, 500, 400)
        self.setStyle(QStyleFactory.create('Fusion'))

        # Set soft color background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))  # Light grey background
        self.setPalette(palette)

        # Layout
        layout = QVBoxLayout()

        # Title
        self.title = QLabel("Generate Secure Password", self)
        self.title.setFont(QFont('Arial', 24))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        # Password length slider
        self.length_label = QLabel("Password Length: 8")
        self.length_slider = QSlider(Qt.Horizontal)
        self.length_slider.setRange(8, 32)
        self.length_slider.setValue(8)
        self.length_slider.setTickPosition(QSlider.TicksBelow)
        self.length_slider.setTickInterval(4)
        self.length_slider.valueChanged.connect(self.update_length)
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_slider)

        # Checkboxes for customization
        self.include_uppercase = QCheckBox("Include Uppercase Letters")
        self.include_numbers = QCheckBox("Include Numbers")
        self.include_symbols = QCheckBox("Include Symbols")
        layout.addWidget(self.include_uppercase)
        layout.addWidget(self.include_numbers)
        layout.addWidget(self.include_symbols)

        # Generate Button
        self.generate_btn = QPushButton("Generate Password")
        self.generate_btn.setStyleSheet("background-color: #5a9; color: white; font-weight: bold; padding: 10px; border-radius: 8px;")
        self.generate_btn.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_btn)

        # Generated password display
        self.password_output = QLineEdit(self)
        self.password_output.setPlaceholderText("Your generated password will appear here")
        self.password_output.setReadOnly(True)
        layout.addWidget(self.password_output)

        # Copy button
        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; border-radius: 8px;")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_btn)

        self.setLayout(layout)

    def update_length(self):
        length = self.length_slider.value()
        self.length_label.setText(f"Password Length: {length}")

    def generate_password(self):
        length = self.length_slider.value()
        characters = string.ascii_lowercase
        if self.include_uppercase.isChecked():
            characters += string.ascii_uppercase
        if self.include_numbers.isChecked():
            characters += string.digits
        if self.include_symbols.isChecked():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_output.setText(password)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_output.text())
        QMessageBox.information(self, "Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
