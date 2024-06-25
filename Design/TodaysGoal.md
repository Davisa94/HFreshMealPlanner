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
6/24/24
=======
Generate a text Document with the same name as the pdf that includes the recipes values in JSON format in the same output directory.
Values to populate today:
    - Recipe Name
    - subtitle
    - prep time
    - cook time
    - calories
    - Stretch:
      - ingredients
      - steps
- Steps
   - generate a function that serializes the values of the recipe card into JSON format.
   - generate a function that reads in the JSON file and returns the values for the recipe card.
   - Update the areas to extract the values for the relevant areas
     - subtitle
     - prep time
     - cook time
     - calories
   - write a function in file managment that reads in the JSON file and returns the values for the recipe card.
   - write a function in file managment that takes the values of the recipe card and writes it to a JSON file.
=======
6/25/24
=======
 - Research and problem solve these issues:
   - certain characters not being detected like 4 with open top, and fraction numbers.
   - Determine how to merge detected text areas that are close enough in a certain x and y direction to be considered a single area using cv2
     - https://stackoverflow.com/questions/55376338/how-to-join-nearby-bounding-boxes-in-opencv-python
     - Going to need to use trigenometry to find text areas that are within a certain distance of each other and merge them.
 - If no viable solution found move on to setting up a database to house the valid data that we can fetch from the image.