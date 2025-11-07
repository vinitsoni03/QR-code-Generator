# QR-code-Generator
A simple yet powerful QR Code Generator built with Python.
It provides:

🖥️ A GUI interface using Tkinter

🧩 Logo overlay support (add your brand logo in the center of QR)

📑 Batch generation from CSV files

🚀 Features

✅ Single QR Generator – Create a QR code from text or URL
✅ Logo Support – Overlay a logo or image at the center of your QR
✅ Batch Mode – Automatically generate multiple QR codes from a CSV file
✅ Preview Window – Instantly view your generated QR in the GUI
✅ Custom Save Location – Choose where to save each QR file

🛠️ Requirements

Make sure you have Python 3.8+ installed.
Then install the required libraries:

pip install qrcode[pil] pillow pandas

📂 Project Structure
qr-code-generator/
│
├── qr_generator_full.py   # Main script with GUI + logo + batch mode
├── sample.csv             # Example CSV for batch mode
├── logo.png               # Optional logo file (example)
└── README.md              # Documentation

🖥️ How to Run
🟢 Run the GUI App
python qr_generator_full.py

🧩 Using the App
1️⃣ Generate Single QR Code

Enter text or a URL in the input box

Click Choose Logo (optional) to add a logo

Click Generate QR

Choose where to save it (.png recommended)

The generated QR code preview appears in the app

2️⃣ Batch QR Generation (CSV Mode)

You can generate multiple QR codes at once from a CSV file.

Example CSV format:

text,filename
https://example.com,example_qr.png
Hello World,hello.png


Steps:

Click Select CSV File and choose your .csv file

Click Select Output Folder and pick the save directory

(Optional) Choose a logo

Click Generate Batch

Each QR will be saved in your selected folder with the specified filenames.

🖼️ Example Output
Example	Description

	Basic QR Code

	QR with logo overlay (example only)
⚙️ Configuration

You can customize:

Error Correction: Currently uses ERROR_CORRECT_H (highest, suitable for logos)

Box Size & Border: Change in the script for different QR sizes

Fill & Background Colors: Can be modified in the generate_qr() function

🧑‍💻 Author

Vinit Soni
💡 Created for learning and demonstration purposes
📚 Includes Python GUI, file handling, and image processing concepts

📜 License

This project is released under the MIT License — you’re free to use, modify, and distribute it.
