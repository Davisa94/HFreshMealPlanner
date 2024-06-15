# Given an input directory get text from the images
import easyocr
import cv2
import os
import numpy as np
from PIL import Image
from hdbscan import HDBSCAN
import fitz

og_files_dir = "EasyOCRSandbox/EasyOCRSandboxOutput/og"

def draw_bounding_boxes(image, detections, threshold=0.25):

    for bbox, text, score in detections:

        if score > threshold:

            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

            cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (255, 0, 0), 2)


def create_searchable_pdf(image, detections, threshold=0.25):

    for bbox, text, score in detections:

        if score > threshold:

            # Create a PDF document
            doc = fitz.Document()

            # Get the bounding box coordinates
            x, y, w, h = bbox
            # Create a new page in the PDF document
            page = doc.new_page(width=image.shape[1], height=image.shape[0])

            # Draw the bounding box on the page
            page.draw_rect(fitz.Rect(x[0], y[0], w[0], h[0]))

            text_position = fitz.Point(x[0], y[0])

            # Set the size of the text
            text_position.z = 12

            # Convert the text to a string
            text_str = str(text)

            # Insert the text on the page
            page.insert_text(text=text_str, point=text_position)

            # Save the PDF document
            doc.save('searchable_pdf.pdf')


def group_detections(detections, threshold=10):
    # Define a function to calculate the distance between two detections
    def distance(bbox1, bbox2):
        x1, y1, w1, h1 = bbox1
        x2, y2, w2, h2 = bbox2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Extract the bounding box coordinates from the detections
    bboxes = [bbox[0] for bbox in detections]

    # Use HDBSCAN clustering algorithm to group the detections
    clusterer = HDBSCAN(min_cluster_size=2, min_samples=1)
    clusterer.fit(bboxes)

    # Create a dictionary to store the groups
    groups = {}

    # Loop through the clusters
    for cluster_id in np.unique(clusterer.labels_):
        # Check if the cluster is noise
        if cluster_id == -1:
            continue
        # Get the detections in the cluster
        cluster_detections = [detections[i] for i in range(len(detections)) if clusterer.labels_[i] == cluster_id]
        # Loop through the detections in the cluster
        for i in range(len(cluster_detections)):
            # Loop through the detections in the cluster
            for j in range(i + 1, len(cluster_detections)):
                # Calculate the distance between the two detections
                dist = distance(cluster_detections[i][0], cluster_detections[j][0])
                # Check if the distance is less than the threshold
                if dist < threshold:
                    # Add the detections to the same group
                    if cluster_id not in groups:
                        groups[cluster_id] = []
                    groups[cluster_id].append(cluster_detections[i])
                    groups[cluster_id].append(cluster_detections[j])

    return groups

def draw_groups(image, groups):
    for group in groups:
        for bbox in groups[group]:
            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
            cv2.putText(image, str(group), tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (255, 0, 0), 2)


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
    og_image = cv2.imread(os.path.join(og_files_dir, file))
    image = cv2.imread(os.path.join(directory, file))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}", thresh)
    # output.extend(reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}"))
    text_detections = reader.readtext(f"EasyOCRSandbox/EasyOCRSandboxOutput/thresh{file}", )
    output.append(text_detections)
    # show the bounding boxes
    threshold = 0.5
    # create_searchable_pdf(og_image, text_detections, threshold=threshold)
    draw_bounding_boxes(image, text_detections, threshold=threshold)
    cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/vis{file}", image)
    # Group the detections
    # groups = group_detections(output, threshold=10)
    # draw_groups(og_image, groups)
    # cv2.imwrite(f"EasyOCRSandbox/EasyOCRSandboxOutput/visGroup{file}", image)




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
