# Given an input directory get text from the images
import easyocr
import cv2
import os
import numpy as np
from PIL import Image


def draw_bounding_boxes(image, detections, threshold=0.25):

    for bbox, text, score in detections:

        if score > threshold:

            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

            cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (255, 0, 0), 2)


def group_detections(detections, threshold=10):
    # Define a function to calculate the distance between two detections
    def distance(bbox1, bbox2):
        x1, y1, w1, h1 = bbox1
        x2, y2, w2, h2 = bbox2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Use DBSCAN clustering algorithm to group the detections

# directory of images
directory = "EasyOCRSandbox/EasyOCRSandboxOutput/OCRInput"

# check if directory exists
if not os.path.exists(directory):
    print(f"Directory {directory} does not exist.")
    exit(1)

# get list of files in directory
files = os.listdir(directory)

# check if directory is empty
if len(files) == 0:
    print(f"Directory {directory} is empty.")
    exit(1)

# Read the images and apply OCR with EasyOCR assume incoming images are grayscale already.
reader = easyocr.Reader(['en'])
output = []
for file in files:
    image = cv2.imread(os.path.join(directory, file))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}", thresh)
    # output.extend(reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}"))
    text_detections = reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}")
    output.append(text_detections)
    # show the bounding boxes
    threshold = 0.5
    draw_bounding_boxes(image, text_detections, threshold=threshold)
    cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/vis{file}", image)



# For each image create a visualization with bounding boxes:
# for i, result in enumerate(output):
#     image = cv2.imread(os.path.join(directory, files[i]))

#     for i, result in enumerate(output):
#         print(f"Result {i}: {result}")
#         print(f"Text {i}: {result[1]}")

#         for bbox, text, prob in result:
#             x, y, w, h = bbox
#             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#         cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/vis{files[i]}", image)
# assume result format is like this: ([[...], [...], [...], [...]], 'HELLO', 0.9993138998921303)
# for i, result in enumerate(output):
#     if i < len(files):
#         image = cv2.imread(os.path.join(directory, files[i]))
#         bbox = result[0]
#         text = result[1]
#         prob = result[2]
#         print (f"Result {i}: {bbox=}, {text=}, {prob=}")
#         print(f"Text {i}: {text=}")
#         x, y, w, h = bbox
#         cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
#         cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)
#     cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/vis{files[i]}", image)
