# PDF Data Extraction Tool

## Overview
This tool is designed to extract detailed information about furniture products from PDF documents. It processes PDFs with a similar content structure and outputs the extracted data in both JSON and CSV formats. Additionally, the tool extracts images embedded in the PDFs.

## Features
- **Text Extraction:** Extracts product details such as product name, description, dimensions, and image links.
- **Image Extraction:** Detects and saves images from PDF pages.
- **Modular Design:** Easily extendable to handle additional product data or adjust to layout variations.
- **Output Formats:** Exports data in JSON and CSV formats.

## Requirements
- Python 3.6+
- Libraries:
  - `pypdf`
  - `PyMuPDF` (fitz)
  - `pandas`
  - `Pillow` (for image processing)
  - `re` (built-in)
  - `json` (built-in)
  - `os` (built-in)

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
