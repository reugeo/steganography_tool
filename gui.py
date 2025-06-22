import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QInputDialog
from embed_detect import embed_message, detect_message

class SteganographyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Steganography Tool")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Select a file to embed or detect a hidden message.", self)
        self.layout.addWidget(self.label)

        self.embed_button = QPushButton("Embed Message", self)
        self.embed_button.clicked.connect(self.embed_message)
        self.layout.addWidget(self.embed_button)

        self.detect_button = QPushButton("Detect Message", self)
        self.detect_button.clicked.connect(self.detect_message)
        self.layout.addWidget(self.detect_button)

        self.setLayout(self.layout)

    def embed_message(self):
        """Embed a message into an image or file."""
        key = self.get_key_from_user()
        if not key:
            return

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_path:
            message, ok = QInputDialog.getText(self, "Input Message", "Enter the message to embed:")
            if ok:
                output_path, _ = QFileDialog.getSaveFileName(self, "Save Output File", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
                if output_path:
                    embed_message(file_path, message, output_path, key)
                    self.label.setText(f"Message embedded successfully in {output_path}.")

    def detect_message(self):
        """Detect hidden messages in a file."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if not file_path:
            return

        # First detect if there is any hidden message without key
        detection_result = detect_message(file_path)
        if detection_result == "No hidden message detected!":
            self.label.setText("No hidden message detected.")
            return
        elif detection_result == "A message has been detected. To decode it, enter the key.":
            # Show detection message and prompt for key only if message detected
            self.label.setText(detection_result)
            key = self.get_key_from_user()
            if not key:
                return
            decrypted_message = detect_message(file_path, key)
            if decrypted_message == "Decryption failed.":
                self.label.setText("Decryption failed. Invalid key or corrupted message.")
            else:
                self.label.setText(f"Detected Message: {decrypted_message}")
        else:
            # Unexpected result, just show it
            self.label.setText(detection_result)

    def get_key_from_user(self):
        """Prompt the user for the encryption key."""
        key, ok = QInputDialog.getText(self, "Enter Encryption Key", "Enter the key for encryption:")
        if ok and len(key) > 0:
            return key.encode()  # Return the key as bytes
        else:
            self.label.setText("Invalid key. Please enter a valid key.")
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SteganographyApp()
    window.show()
    sys.exit(app.exec_())