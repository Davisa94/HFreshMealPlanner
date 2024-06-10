import cv2
import numpy as np
import os
from pdf2image import convert_from_path

def save_image(image, path):
    cv2.imwrite(path, image)

def rotate_JPEG2(image):
    image = np.array(image)
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return rotated_image

def process_pdf(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    images = convert_from_path(pdf_path)
    # convert images from PIL to OpenCV format
    images = [cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) for image in images]

    # rotate and save images
    for i, image in enumerate(images):
        save_image(image, f"{output_dir}/page{i}.jpg")
        rotated_image = rotate_JPEG2(image)
        save_image(rotated_image, f"{output_dir}/page{i}_rotated.jpg")

# test PDF path
pdf_path = "EasyOCRSandbox/test.pdf"
output_dir = "EasyOCRSandbox/EasyOCRSandboxOutput"

process_pdf(pdf_path, output_dir)