6/22/24
=======
Read in the image pdf in and then rename the pdf to the recipe name saved to an output folder.
Break it down:
    Step 1: Create a function to read in the pdf
    Step 2: Create a function to read the text from the pdf into an array of detections with bounding boxes
    Step 3: Create a function to extract the text from the detections based on the bounding boxes
        step 3a: Create a list of areas to extract text from i.e the name of the recipe is any bounding boxes within a set area.
    Step 4: take the name of the recipe and rename the input file and save it in the output folder
=======