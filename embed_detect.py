from PIL import Image
from cryptography.fernet import Fernet

def get_key_from_user():
    """Prompt the user for the encryption key."""
    key, ok = QInputDialog.getText(None, "Enter Encryption Key", "Enter the key for encryption:")
    if ok and len(key) > 0:
        return key.encode()  
    else:
        print("Key input failed or empty key!")
        return None

def message_to_bin(message):
    """Convert a message string to a binary string."""
    return ''.join(format(ord(i), '08b') for i in message)

def bin_to_message(binary_message):
    """Convert a binary string back to the original message."""

    if len(binary_message) % 8 != 0:
        print(f"Error: Binary message length is not a multiple of 8.")
        return None
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encrypt_message(message, key):
    """Encrypt a message using Fernet encryption."""
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, key):
    """Decrypt a message using Fernet encryption."""
    cipher = Fernet(key)
    try:
        return cipher.decrypt(encrypted_message.encode()).decode()
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None

def embed_message(file_path, message, output_path, key):
    """Embed a message into an image or other file using the LSB method."""
    img = Image.open(file_path)
    img = img.convert("RGB")  

    encrypted_message = encrypt_message(message, key)
    binary_message = message_to_bin(encrypted_message) + '1111111111111110'  # End-of-message delimiter
    message_length = len(binary_message)
    print(f"Binary encrypted message to embed: {binary_message}")  # Debugging output

    pixels = img.load()
    width, height = img.size
    pixel_index = 0

    for row in range(height):
        for col in range(width):
            if pixel_index >= message_length:
                break

            pixel = list(pixels[col, row])  
            for channel in range(3):  
                if pixel_index < message_length:
                    bit = int(binary_message[pixel_index])
                    pixel[channel] = (pixel[channel] & 0xFE) | bit
                    pixel_index += 1
            pixels[col, row] = tuple(pixel)  # Update the pixel with modified values

    img.save(output_path)
    print(f"Message embedded successfully in {output_path}.")

def detect_message(file_path, key=None):
    """Detect a hidden message in an image using the LSB method."""
    img = Image.open(file_path)
    img = img.convert("RGB")  # Ensure the image is in RGB mode

    pixels = img.load()
    width, height = img.size

    binary_message = ''
    found = False

    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]
            for channel in range(3):  # Extract LSB 
                binary_message += str(pixel[channel] & 1)

                # Check for end-of-message delimiter
                if len(binary_message) >= 16 and binary_message[-16:] == '1111111111111110':
                    found = True
                    break
            if found:
                break
        if found:
            break

    if not found:
        print("No hidden message detected!")
        return "No hidden message detected!"

    # If message is found and no key provided, just notify detection
    if key is None:
        print("A message has been detected. To decode it, enter the key.")
        return "A message has been detected. To decode it, enter the key."

    decrypted_message = decrypt_message(bin_to_message(binary_message[:-16]), key)
    if decrypted_message:
        return decrypted_message
    else:
        print("Decryption failed.")
        return "Decryption failed."
