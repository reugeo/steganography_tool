#  Steganography Tool —  Message Hiding and Detection in Images

##  Overview
This project is an advanced **graphical steganography tool** that enables users to securely embed and detect **encrypted messages** inside image files using a powerful combination of **Least Significant Bit (LSB) manipulation** and **Fernet symmetric encryption**.

Designed with **non-technical users in mind**, the tool features an intuitive **GUI built with PyQt5**, making it accessible while retaining robust security under the hood.

---

##  How It Works

###  Embedding Process
- User writes a secret message and provides an encryption key.
- The message is **encrypted using Fernet** (symmetric AES).
- Encrypted data is **converted to binary** and hidden in the **least significant bits** of the image pixels.
- A **custom end-of-message binary delimiter** is added to detect message boundaries.

###  Detection Process
- The tool scans the image for the **binary delimiter**.
- If found, it extracts the binary data, converts it back to text, and decrypts it using the user-provided key.
- If no key is provided or it's incorrect, the tool **notifies the user** of the presence of a hidden message.

###  Graphical Interface (GUI)
Built with **PyQt5**, the GUI allows:
- Image selection for embedding or detection
- Message and key entry
- Easy saving of output images
- Real-time status updates

---

##  Unique Use Cases
| Scenario | Description |
|---------|-------------|
|  Artistic Secret Sharing | Embed hidden stories or provenance in digital artworks |
|  Personalized Gifts | Send photos with embedded private notes for birthdays, anniversaries |
|  Secure Education | Distribute image-based clues, accessible only with the correct key |
|  Geo-Caching | Hide treasure hunt clues in images |
|  Medical Imaging | Embed encrypted patient info directly into X-ray or scan files |

---

## Advantages
-  **Double Layer Security**: Combines encryption and steganography
-  **User-Friendly GUI**: No coding or terminal required
-  **Supports PNG, JPG, BMP**
-  **Instant Feedback**: Clear user alerts and decryption guidance
-  **Custom Delimiter**: Unique marker (`1111111111111110`) minimizes false reads

---

## Limitations
-  **Message Size is Limited** by image resolution and format
-  **Lost Keys = Lost Messages**
-  **Image Quality Slightly Alters**, especially for small or compressed images
-  **One Message per Image** due to single delimiter usage
-  **Undetectable by Common Tools**, which is good for secrecy but bad for discovery

---

## Real-Life Applications
-  **Private Communication** via social media or email
-  **Digital Watermarking** without visible overlay
-  **Forensics & Legal Chain-of-Custody** data embedding
-  **Corporate Security** to detect unauthorized data leaks
-  **Museum Archiving** metadata embedded in digital exhibits

---

##  Getting Started

### Launch the Tool

-pip install -r requirements.txt

-python gui.py
