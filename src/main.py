# import generateTextAreas
import shutil
from GenerateTextAreas import *
from FileManagment import *
from RecipeCard import *

import sys


# # First we get the directory from the first argument

# directory = sys.argv[1]

# # Then we open the folder and get the files
# files = get_files(directory)

# # Then we generate the text areas
# generate_text_areas(file)

# # Then we sort the data

# # First we need to generate the text areas



def main():
    print("Processing files...")
    # setup array to hold recipe cards
    recipe_cards = []
    # # First we get the directory from the first argument
    # directory = sys.argv[1]
    # # Then we open the folder and get the files
    # files = get_files(directory)
    # # Then we generate the text areas
    # generate_text_areas(files)
    Input_directory = "EasyOCRSandbox/EasyOCRSandboxInput"
    Output_directory = "EasyOCRSandbox/EasyOCRSandboxOutput/RenamedPDFs"
    # make the output directory if not exists
    os.makedirs(Output_directory, exist_ok=True)
    # get a list of files in the directory
    files = get_files(Input_directory)
    # for each file, generate the text areas
    for i, file in enumerate(files):
        recipe_cards.append(generate_text_areas(file))
        recipe_cards[i].set_initial_path(file)
        print(recipe_cards[i].get_recipe_name())
        recipe_cards[i].set_new_path(f"{Output_directory}/{recipe_cards[i].get_recipe_name()}.pdf")
        print(file)
        # save the original pdf as a copy in the output directory
        # shutil.copy(file, recipe_cards[i].get_new_path())
        # rotate the image 90 degrees counter-clockwise and save it to the output directory
        rotate_PDF(file, recipe_cards[i].get_new_path())
        # save the pdf in the output directory
        # recipe_cards[i].save_pdf()
        # serialize the recipe card
        card_data = serialize_card(recipe_cards[i])
        save_JSON(card_data, recipe_cards[i].get_new_path())

    print("Done!")


if __name__ == "__main__":
    main()