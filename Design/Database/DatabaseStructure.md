Recipe:
    - recipe_id
    - Name: Required
    - Subtitle: Required
    - Prep time
    - cook time
    - Calorie Estimate

Tags: (auto generated using AI ideally):
    - tag
    - description


Ingredient:
    - Ingredient_id
    - name

Recipe_Ingredients:
    - Recipe_Id
    - Ingredient_id
    - amount_2
    - amount_4
    - unit (i.e tbsp, oz, pinch, whole(vegetable, fruit, egg..., ))

step:
    - step_id
    - description (i.e Wash, cut, peel, preheat, Boil Spaghetti with salt, and oil),

Recipe_Step table: (each step can have multiple ingredients)
    - step_id
       - ingredient_id
       - appliance_id
       - cookware_id
       - utensil_id

Appliance
    - appliance_id
    - name


