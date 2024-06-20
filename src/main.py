# import generateTextAreas
from GenerateTextAreas import *
from FileManagment import *

import sys


# First we get the directory from the first argument

directory = sys.argv[1]

# Then we open the folder and get the files
files = get_files(directory)

# Then we generate the text areas
generate_text_areas(files)

# Then we sort the data

# First we need to generate the text areas


