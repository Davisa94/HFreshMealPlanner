#Generate classes to hold that data in a format that can be inserted into the database
# Recipe:
#     - recipe_id
#     - Name: Required
#     - Subtitle: Required
#     - Prep time
#     - cook time
#     - Calorie Estimate

# Tag:
#     - tag_id
#     - tag_name
#     - description

# Recipe_tags:
#     - tag_id
#     - recipe_id

# Ingredient:
#     - Ingredient_id
#     - name
#     - description (optional)

# Recipe_Ingredients:
#     - Recipe_Id
#     - Ingredient_id
#     - amount_2 
#     - amount_4
#     - unit (i.e tbsp, oz, pinch, whole(vegetable, fruit, egg..., ))

# Step:
#     - step_id
#     - description (i.e Wash, cut, peel, preheat, Boil Spaghetti with salt, and oil),

# Cookware_table
#     - cookware_id
#     - name
#     - status (optional, do you have it for example,)

# Recipe_Step table: (each step can have multiple ingredients)
#     - step_id
#     - ingredient_id
#     - appliance_id
#     - cookware_id
#     - utensil_id

# Appliance
#     - appliance_id
#     - name

# TODO we may need to use an AI API to determine which of the 'Bust out' things are cookware, appliances, and utensils, and to parse the steps to find appliances, utensils, and cookware to populate the class.

# Recipe Card class
def recipe_card():
    def __init__(self):
        self.recipe_name
        self.subtitle
        self.prep_time
        self.cook_time
        self.calorie_estimate
        self.ingredients
        self.steps
        self.tags
        self.cookware
        self.appliances
        self.utensils
        # name: (x1, y1, x2, y2) Bounding boxes
        self.card_areas = {
            "name": (0, 0, 0, 0),
            "subtitle": (0, 0, 0, 0),
            "prep_time": (0, 0, 0, 0),
            "cook_time": (0, 0, 0, 0),
            "calorie_estimate": (0, 0, 0, 0),
            "ingredients": (0, 0, 0, 0),
            "steps": (0, 0, 0, 0),
            "description": (0, 0, 0, 0),
            "bust_out": (0, 0, 0, 0)
        }
    def get_recipe_name(self, found_text):
    # TODO we need to parse the text to find the name of the recipe card by finding the first (highest y) bounding box that has text
        pass