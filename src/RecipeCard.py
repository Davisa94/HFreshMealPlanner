import re


class RecipeCard:
    def __init__(self):
        self.front_page = []
        self.back_page = []
        self.initial_path = None
        self.final_path = None
        self.recipe_name = None
        self.subtitle = None
        self.prep_time = None
        self.cook_time = None
        self.calorie_estimate = None
        self.ingredients = None
        self.steps = None
        self.tags = None
        self.cookware = None
        self.appliances = None
        self.utensils = None
        self.card_areas = {
            "name": ([2715, 0], [9120, 500]),
            "subtitle": ([2715,400], [9136,671]),
            "prep_time": ([4054,6518],  [5610, 6865]),
            "cook_time": ([5230,6518], [6853,6865]),
            "calorie_estimate": ([6300,6518], [7990,6865]),
            "ingredients": ([0,1111], [3100,4835]),
            "steps": ([2233,0], [9145,7050]),
            "description": ([0,0 ], [0, 0]),
            "bust_out": ([0, 0], [0, 0])
        }


    def get_card_areas(self):
        return self.card_areas
        
    def base_getters(self,page,member_name, card_area_name):
        # Given the self.detections list is populated, find the detection whose bounding box is closest to the area in self.card_areas[name]
        # first we verify that self.front_page and self.back_page are populated
        if len(self.front_page) == 0 or len(self.back_page) == 0:
            return None
        # verify if our name has already been set
        member_value = getattr(self, member_name)
        if member_value is not None:
            return member_value
        for detection in page:
            if is_within_area(detection[0], self.card_areas[card_area_name]):
                # set our name to the text in the detection
                setattr(self, member_name, detection[1])
                member_value = getattr(self, member_name)
                return detection[1]
            
    def get_recipe_name(self):
        return self.base_getters(self.front_page, "recipe_name", "name")

    def get_subtitle(self):
        return self.base_getters(self.front_page, "subtitle", "subtitle")

    def get_prep_time(self):
        self.base_getters(self.front_page, "prep_time", "prep_time")
        self.prep_time = strip_non_numerics(self.prep_time)
        return self.prep_time

    def get_cook_time(self):
        self.base_getters(self.front_page, "cook_time", "cook_time")
        self.cook_time = strip_non_numerics(self.cook_time)
        return self.cook_time

    def get_calorie_estimate(self):
        self.base_getters(self.front_page, "calorie_estimate", "calorie_estimate")
        self.calorie_estimate = strip_non_numerics(self.calorie_estimate)
        return self.calorie_estimate

    def get_ingredients(self):
        return self.base_getters(self.front_page, "ingredients", "ingredients")

    def get_steps(self):
        return self.base_getters(self.front_page, "steps", "steps")

    def add_front_detection(self, detection):
        self.front_page.append(detection)

    def add_back_detection(self, detection):
        self.back_page.append(detection)

    def get_front_page(self):
        return self.front_page

    def get_back_page(self):
        return self.back_page
    
    # set and get initial path
    def set_initial_path(self, path):
        self.initial_path = path
    
    def get_initial_path(self):
        return self.initial_path
    
    # set and get final path
    def set_final_path(self, path):
        self.final_path = path
    
    def get_final_path(self):
        return self.final_path
    
    # set and get new path
    def set_new_path(self, path):
        self.final_path = path
    
    def get_new_path(self):
        return self.final_path

# serliealize card into json format
def serialize_card(card):
    # create JSON object
    json_object = {
        "name": card.get_recipe_name(),
        "subtitle": card.get_subtitle(),
        "prep_time_mins": card.get_prep_time(),
        "cook_time_mins": card.get_cook_time(),
        "calorie_estimate": card.get_calorie_estimate(),
        "ingredients": card.get_ingredients(),
        "steps": card.get_steps()
    }
    return json_object

# deserialize card from json format
def deserialize_card(json_object):
    card = RecipeCard()
    card.recipe_name = json_object["name"]
    card.subtitle = json_object["subtitle"]
    card.prep_time = json_object["prep_time"]
    card.cook_time = json_object["cook_time"]
    card.calorie_estimate = json_object["calorie_estimate"]
    card.ingredients = json_object["ingredients"]
    card.steps = json_object["steps"]
    card.tags = json_object["tags"]
    card.cookware = json_object["cookware"]
    card.appliances = json_object["appliances"]
    card.utensils = json_object["utensils"]
    return card

def is_within_area(coord1, coord2):
    x1_min, y1_min = min(coord1[0][0], coord1[1][0]), min(coord1[0][1], coord1[2][1])
    x1_max, y1_max = max(coord1[0][0], coord1[1][0]), max(coord1[0][1], coord1[2][1])

    x2_min, y2_min = coord2[0][0], coord2[0][1]
    x2_max, y2_max = coord2[1][0], coord2[1][1]

    return x2_min <= x1_min and y2_min <= y1_min and x2_max >= x1_max and y2_max >= y1_max

def strip_non_numerics(string):
    return ''.join(char for char in string if char.isdigit())