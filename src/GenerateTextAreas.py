import easyocr
import cv2
import os
import numpy as np
from pdf2image import convert_from_path
from RecipeCard import RecipeCard



def generate_text_areas(input_pdf_path):
    images = convert_from_path(input_pdf_path)
    # set up our recipe card object
    recipe_card = RecipeCard()

    for i, image in enumerate(images):
        images[i] = rotate_JPEG2(image)
    
    reader = easyocr.Reader(['en'], gpu=True)

    for i, image in enumerate(images):
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}{input_pdf_path[-4:]}.jpg", thresh)
        output = reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}{input_pdf_path[-4:]}.jpg")
        # if this is the first image add output to the front page of the recipe card
        if i == 0:
            recipe_card.front_page = output
        # if this is not the first image add output to the back page of the recipe card
        else:
            recipe_card.back_page = output
    return recipe_card



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
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def rotate_JPEG2(image):
    image = np.array(image)
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return rotated_image

# function to save a given image to a given path
def save_image(image, path):
    cv2.imwrite(path, image)

# test image path
# testPDFPath = "../EasyOCRSandbox/test.pdf"

# # Create a directory for the output
# os.makedirs("EasyOCRSandbox", exist_ok=True)

# # Create a directory for the output
# os.makedirs("EasyOCRSandbox/EasyOCRSandboxOutput", exist_ok=True)

# Convert the PDF to images
# images = convert_from_path(testPDFPath)

# # rotate the JPEG image 90 degrees counter-clockwise
# for i, image in enumerate(images):
#     images[i] = rotate_JPEG2(image)
#     # save the images
#     save_image(images[i], f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg")
    # image = np.array(image)
    # cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg", image)

    # image.save(f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg", "JPEG")

# Check if a GPU is available

# # Read the images and apply OCR
# reader = easyocr.Reader(['en'], gpu=True)
# output = []
# for i in range(len(images)):
#     image = cv2.imread(f"EasyOCRSandbox/EasyOCRSandboxOutput/page{i}.jpg")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#     cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}.jpg", thresh)
#     output.extend(reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{i}.jpg"))

# # Print the output
# print(output)

# # Save the output
# with open("EasyOCRSandbox/EasyOCRSandboxOutput/output.txt", "w") as f:
#     for line in output:
#         f.write(line[1] + "\n")