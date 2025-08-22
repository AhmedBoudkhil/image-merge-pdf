# image-merge-pdf
A simple Python tool to convert multiple images (WEBP, PNG, JPG, JPEG, BMP, TIFF) into a single PDF file. Supports numeric ordering (######1, ######2...) or falls back to alphabetical.


# 🖼️ Image to PDF Converter

A lightweight Python script that converts multiple images into a single PDF file.  
Supports `.webp`, `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.tiff` formats.  

It automatically sorts files numerically if filenames contain `######<number>`,  
otherwise it falls back to alphabetical order.

---

## 🚀 Features
- ✅ Convert multiple image formats into **one PDF**
- ✅ Supports `.webp`, `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`
- ✅ Keeps images in **numeric order** if filenames use `######<number>`
- ✅ Works on **Linux, macOS, Windows**

---

## 🔧 Installation
Clone the repo and install the required dependency:

```bash
git clone https://github.com/yourusername/image-to-pdf.git
```
## 📂 Usage

```bash
python3 convert.py /path/to/images output.pdf
```

## 📜 Example Filenames
img1######1.webp 
img2######1.webp 
img3######3.webp 

.

## 📝 Requirements

Python 3.7+

Pillow
```bash
pip install -r requirements.txt

```
```bash
cd image-to-pdf
pip install -r requirements.txt
```
