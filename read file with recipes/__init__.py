from model import Ingredient
from model import Dish
import reader

cook_book = {}
dish_list = []

counter = 0
tmp_name = ""
for element in reader.read_file("recipes.txt"):
    if element == "\n":
        counter = 0
        continue
    elif counter == 0:
        dish = Dish.Dish()
        dish.set_name(element)
        dish_list.append(dish)
        counter += 1
        tmp_name = element
        continue
    elif counter == 1:
        for el in dish_list:
            if el.get_name() == tmp_name:
                el.set_persons(element)
                break
        counter += 1
    elif counter > 1:
        ingredient_list = element.split(" | ")
        ingredient = Ingredient.Ingredient()
        ingredient.set_ingredient_name(ingredient_list[0])
        ingredient.set_quantity(ingredient_list[1])
        ingredient.set_measure(ingredient_list[2])
        for el in dish_list:
            if el.get_name() == tmp_name:
                a = el.get_ingredients()
                a.append(ingredient)
                el.set_ingredient(a)
                break

for dish in dish_list:
    ingredient_list_2 = []
    cook_book[dish.get_name()] = ingredient_list_2
    for element in dish.get_ingredients():
        ingredient_dict = {}
        ingredient_dict['ingredient_name'] = element.get_ingredient_name()
        ingredient_dict['quantity'] = element.get_quantity()
        ingredient_dict['measure'] = element.get_measure()
        ingredient_list_2.append(ingredient_dict)

print(cook_book)
