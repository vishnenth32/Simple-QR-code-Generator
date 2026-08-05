# QR Code Generator
A simple Python project that generates a QR code from a given text or URL using the `qrcode` library.

## Features
- Generate QR codes from text or URLs.
- Save the QR code as a PNG image.
- Easy to customize the input data.

## Requirements
- Python 3.x
- qrcode
- Pillow

## Installation
Install the required libraries using pip:
```bash
pip install qrcode
pip install pillow
```

## Output
After running the program, a file named `qrcode.png` will be created in the project directory. Scan the QR code using any QR scanner to view the stored information.

## Project Structure
```
QR-Code-Generator/
│── create_qrcode.py
│── qrcode.png
└── README.md
```

## Example
**Input:**
```
https://github.com/yourusername
```

**Output:**
A QR code image (`qrcode.png`) that opens the GitHub profile when scanned.

⭐ Feel free to fork this project, improve it, and share it with others!
