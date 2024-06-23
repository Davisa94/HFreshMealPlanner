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
            "prep_time": ([0, 0], [0, 0]),
            "cook_time": ([0, 0], [0, 0]),
            "calorie_estimate": ([0, 0], [0, 0]),
            "ingredients": ([0, 0], [0, 0]),
            "steps": ([0, 0], [0, 0]),
            "description": ([0, 0], [0, 0]),
            "bust_out": ([0, 0], [0, 0])
        }

    def get_card_areas(self):
        return self.card_areas
    

    def get_recipe_name(self):
        # Given the self.detections list is populated, find the detection whose bounding box is closest to the area in self.card_areas[name]
        # first we verify that self.front_page and self.back_page are populated
        if len(self.front_page) == 0 or len(self.back_page) == 0:
            return None
        # verify if our name has already been set
        if self.recipe_name is not None:
            return self.recipe_name
        # TODO we need to parse the text to find the name of the recipe card by finding the first (highest y) bounding box that has text
        # loop through self.front_page
        # if the bounding box is within the area in self.card_areas[name]
        # return the text in the detection
        # else return None
        for detection in self.front_page:
            if is_within_area(detection[0], self.card_areas["name"]):
                # set our name to the text in the detection
                self.recipe_name = detection[1]
                return self.recipe_name
        

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
    

def is_within_area(coord1, coord2):
    x1_min, y1_min = min(coord1[0][0], coord1[1][0]), min(coord1[0][1], coord1[2][1])
    x1_max, y1_max = max(coord1[0][0], coord1[1][0]), max(coord1[0][1], coord1[2][1])

    x2_min, y2_min = coord2[0][0], coord2[0][1]
    x2_max, y2_max = coord2[1][0], coord2[1][1]

    return x2_min <= x1_min and y2_min <= y1_min and x2_max >= x1_max and y2_max >= y1_max