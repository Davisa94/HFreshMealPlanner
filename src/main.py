# import generateTextAreas
from GenerateTextAreas import *
from FileManagment import *

import sys


# First we get the directory from the first argument

directory = sys.argv[1]

# Then we open the folder and get the files
files = get_files(directory)

# Then we generate the text areas
generate_text_areas(file)

# Then we sort the data

# First we need to generate the text areas



def main():
    # # First we get the directory from the first argument
    # directory = sys.argv[1]
    # # Then we open the folder and get the files
    # files = get_files(directory)
    # # Then we generate the text areas
    # generate_text_areas(files)
    Input_directory = "EasyOCRSandbox/EasyOCRSandboxInput"
    Output_directory = "EasyOCRSandbox/EasyOCRSandboxOutput"
    # get a list of files in the directory
    files = get_files(Input_directory)
    # for each file, generate the text areas
    for file in files:
        generate_text_areas(file)



if __name__ == "__main__":
    main()