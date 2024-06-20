# A module that has various functions for PDF generation and management
import os
import pathlib
import shutil
from pdf2image import convert_from_path
import torch
import fitz
import pymupdf



# Given an array of bounding boxes with text, create a PDF with text at those areas.
def create_pdf(detections, output_dir="EasyOCRSandbox/EasyOCRSandboxOutput"):

    for bbox, text, score in detections:

        # Create a PDF document
        doc = fitz.Document()

        # Get the bounding box coordinates
        x, y, w, h = bbox
        # Create a new page in the PDF document
        page = doc.new_page(width=595, height=842)

        # Draw the bounding box on the page
        page.draw_rect(fitz.Rect(x[0], y[0], w[0], h[0]))

        text_position = fitz.Point(x[0], y[0])

        # Set the size of the text
        text_str = str(text)

        # Insert the text on the page
        page.insert_text(text=text_str, point=text_position)

        # Save the PDF document
        doc.save(f"{output_dir}/pdf.pdf")

    print("PDF creation complete!")

def create_basic_pdf(name, output_dir="../EasyOCRSandbox/EasyOCRSandboxOutput"):
    # Create a PDF document
    doc = fitz.Document()

    # Create a new page in the PDF document
    page = doc.new_page(width=595, height=842)\
    
    # Get the page's width and height
    page_width, page_height = page.rect.width, page.rect.height

    # add the text of the name in large font to the middle of the page
    page.insert_text((page_width // 2, page_height // 2), name, fontsize=50, fontname="helv")


    # Save the PDF document
    return doc

# given an x1, y1 and an x2, y2, (bounding box) return a point just inside the bounding box
def bounding_box_2_Point(x1, y1, x2, y2):
    # TODO potential adjustments to make sure the point is inside the bounding box
    p = fitz.Point(x1, y1)
    return p
# given the arguments of the doc, text, x, y, w, h and page number, insert the text on the page.
def insert_text_box(doc, text, page, x, y, w, h):
    # verify the doc has a page at the specified page number
    if page < 0 or page >= doc.page_count:
        raise ValueError(f"Page {page} does not exist in the PDF document.")

    # get the page at the specified page number
    page = doc[page]

    # insert a new shape on the page
    page.insert_textbox(rect = pymupdf.Rect(x, y, w, h), buffer=text, fontsize=10, fontname="helv", align=0)

    # page.commit()
    # save the PDF document
    return doc
    doc.close()


def main():
    name = "test"
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "EasyOCRSandbox", "EasyOCRSandboxOutput"))
    doc = create_basic_pdf(name)
    doc = insert_text_box(doc, "Hello PDF", 0, 50, 50, 300, 150)

    doc.save(os.path.join(directory, name + ".pdf"))
    doc.close()


if __name__ == "__main__":
    main()