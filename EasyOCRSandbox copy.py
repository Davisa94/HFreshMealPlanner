import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import pathlib
import shutil
from pdf2image import convert_from_path
import torch

# test image path
testImagePath = "EasyOCRSandbox/test.pdf"

# Create a directory for the output
os.makedirs("EasyOCRSandbox", exist_ok=True)

# Create a directory for the output
os.makedirs("EasyOCRSandbox/EasyOCRSandboxOutput", exist_ok=True)

# Convert the PDF to images
images = convert_from_path(testImagePath)

# rotate the JPEG image 90 degrees counter-clockwise
def rotate_JPEG(image):
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

for i, image in enumerate(images):
    images[i] = rotate_JPEG(image)
    # save the images
    image.save(f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg", "JPEG")

# Check if a GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Read the images and apply OCR
reader = easyocr.Reader(['en'], gpu=True, device=device)
output = []
for i in range(len(images)):
    image = cv2.imread(f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}.jpg", thresh)
    output.extend(reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}.jpg", gpu=True, device=device))

# Print the output
print(output)

# Save the output
with open("EasyOCRSandbox/EasyOCRSandboxOutput/output.txt", "w") as f:
    for line in output:
        f.write(line[1] + "\n")