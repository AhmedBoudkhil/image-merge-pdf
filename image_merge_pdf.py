#!/usr/bin/env python3
"""
Universal Image to PDF Converter
--------------------------------
This script converts multiple images (WEBP, PNG, JPG, JPEG, BMP, TIFF)
into a single PDF file.

- If filenames contain "######<number>", the script sorts numerically.
- Otherwise, files are sorted alphabetically.

Usage:
    python3 convert.py /path/to/images output.pdf
"""

import os
import re
import sys
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 convert.py <input_folder> <output.pdf>")
        sys.exit(1)

    folder = sys.argv[1]
    output_pdf = sys.argv[2]

    # Allowed image formats
    valid_ext = (".webp", ".png", ".jpg", ".jpeg", ".bmp", ".tiff")

    # Collect all valid images
    files = [f for f in os.listdir(folder) if f.lower().endswith(valid_ext)]

    if not files:
        print("❌ No valid images found in the folder.")
        sys.exit(1)

    # Extract number after ###### if exists
    def extract_number(filename):
        match = re.search(r'######(\d+)', filename)
        return int(match.group(1)) if match else float('inf')

    # Sort: first by extracted number (if any), else alphabetically
    files.sort(key=lambda f: (extract_number(f), f.lower()))

    # Convert to images
    images = [Image.open(os.path.join(folder, f)).convert("RGB") for f in files]

    # Save to PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

    print(f"✅ PDF created: {output_pdf}")

if __name__ == "__main__":
    main()
