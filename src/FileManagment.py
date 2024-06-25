# A module with all the functionality to open files
# and save files

import json
import os
import PyPDF2
from PIL import Image
import pytesseract
import cv2
import easyocr
import numpy as np
from pdf2image import convert_from_path
from pytesseract import Output


#  a function to get and return a list of files in a directory
def get_files(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            files.append(os.path.join(directory, filename))
    return files

# Read in a PDF and rotate it, then save it to the newpath
def rotate_PDF(path, newpath):
    reader = PyPDF2.PdfReader(path)
    writer = PyPDF2.PdfWriter()
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        page.rotate(90)
        writer.add_page(page)
    with open(newpath, 'wb') as f:
        writer.write(f)
    

# takes in a JSON and a filename path and saves it to the given path
def save_JSON(JSON, filename):
    with open(f"{filename}.json", 'w') as f:
        json.dump(JSON, f)

# takes in a filename and opens it returning the contents of the file in json format
def open_JSON(filename):
    with open(f"{filename}.json", 'r') as f:
        return json.load(f)

        