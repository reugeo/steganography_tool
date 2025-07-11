# Steganography Tool — Message Hiding and Detection in Images

## Overview

This project is an advanced **graphical steganography tool** that empowers users to **securely embed and detect encrypted messages inside image files**, combining:

* **Least Significant Bit (LSB) manipulation** for data hiding
* **Fernet symmetric encryption (AES)** for confidentiality

Designed for **non-technical users**, the tool provides an intuitive **PyQt5 graphical interface**, making strong security accessible without requiring programming knowledge.

---

## How It Works

### Embedding Process

1. The user inputs a **secret message** and an **encryption key**.
2. The message is **encrypted using Fernet** (AES symmetric encryption).
3. Encrypted data is **converted to binary**.
4. Binary bits are embedded in the **least significant bits** of the image pixels.
5. A **custom end-of-message binary delimiter** is appended to mark where the hidden message ends.

---

### Detection Process

1. The tool scans the image for the **delimiter**.
2. If a message is detected:

   * Binary data is extracted and reassembled.
   * Data is decrypted with the provided key.
   * If the key is missing or incorrect, the user is alerted that hidden data was found but cannot be read.

---

### Graphical Interface

Built with **PyQt5**, the user interface offers:

* Simple selection of input and output images
* Fields for entering messages and encryption keys
* Real-time status updates during embedding and detection
* Clear error handling and user guidance

---

## Unique Use Cases

| Scenario                       | Description                                                         |
| ------------------------------ | ------------------------------------------------------------------- |
| **Artistic Secret Sharing**    | Embed hidden stories or ownership details in digital art            |
| **Personalized Digital Gifts** | Send photos with private notes for birthdays or anniversaries       |
| **Secure Education**           | Distribute image-based clues accessible only to authorized students |
| **Geo-Caching**                | Hide treasure hunt instructions in images                           |
| **Medical Imaging**            | Embed encrypted patient data into X-rays or scan files              |

---

## Advantages

* **Double Layer Security:** Combines steganography and encryption for enhanced confidentiality.
* **User-Friendly GUI:** No command-line knowledge required.
* **Multi-Format Support:** Works with PNG, JPG, BMP.
* **Custom Delimiter:** Unique binary marker (`1111111111111110`) reduces accidental detection.
* **Immediate Feedback:** Clear alerts when messages are detected or decryption fails.

---

## Limitations

* **Message Size Limited:** Embedding capacity depends on image resolution.
* **Lost Keys = Lost Messages:** Encryption requires the correct key to recover data.
* **Minor Image Alteration:** LSB changes may slightly affect image quality.
* **One Message per Image:** Single delimiter limits embedding to one payload.
* **Undetectable by Common Tools:** Hidden data is not easily discoverable by standard steganalysis (can be a benefit or a drawback).

---

## Real-Life Applications

* **Private Communication:** Share confidential information via email or social media images.
* **Digital Watermarking:** Prove ownership without visible overlays.
* **Forensics & Legal:** Embed chain-of-custody metadata in evidence photos.
* **Corporate Security:** Detect unauthorized data exfiltration in images.
* **Museum & Archive:** Embed provenance or catalog metadata in digital reproductions.

---

## Getting Started

### Installation

First, install the required Python packages:

```sh
pip install -r requirements.txt
```

---

### Launch the Tool

Run the GUI application:

```sh
python gui.py
```

The graphical interface will open, ready for embedding and detection.

---

## Authors

* REUBEN GEORGE
