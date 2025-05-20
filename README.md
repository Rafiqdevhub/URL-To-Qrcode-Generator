# URL to QR Code Generator

A streamlined web application that converts URLs into downloadable QR codes. Built with Python and Streamlit, this application provides an easy way to generate QR codes for any web address.

## Features

- 🌐 Simple URL input interface
- 🔄 Automatic URL formatting (adds https:// if missing)
- 🎨 Clean and modern web interface
- ⬇️ Downloadable QR codes in PNG format
- 🛡️ Input validation and error handling

## Prerequisites

- Python 3.13 or higher
- Required Python packages:
  - streamlit >= 1.45.1
  - qrcode >= 8.2
  - pillow >= 11.2.1

## Installation

Clone the repository:

```powershell
git clone https://github.com/Rafiqdevhub/URL-To-Qrcode-Generator.git
cd "URL-To-Qrcode-Generator"
```

## Usage

1. Start the Streamlit application:

```powershell
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter a URL in the text input field

4. Click the "Generate QR Code" button

5. Download the generated QR code using the "Download QR Code" button

## How It Works

The application uses:

- `streamlit` for the web interface
- `qrcode` library for generating QR codes
- `pillow` for image processing

When a URL is submitted:

1. The application validates and formats the URL
2. Generates a QR code using the qrcode library
3. Displays the QR code in the web interface
4. Provides a download option in PNG format

## Project Structure

```
URL Generator/
├── main.py           # Main application file
├── pyproject.toml    # Project dependencies and metadata
├── README.md         # Documentation
└── .gitignore       # Git ignore file
```
