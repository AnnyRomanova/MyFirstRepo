cook_book = {}


class Dish:

    def __init__(self):
        self.__ingredients = []
        self.__persons = 0
        self.__dish_name = ""

    def set_name(self, dish_name):
        self.__dish_name = dish_name

    def set_persons(self, persons):
        self.__persons = persons

    def set_ingredient(self, ingredients):
        self.__ingredients = ingredients

    def get_name(self):
        return self.__dish_name

    def get_ingredients(self):
        return self.__ingredients

    def print_dish(self):
        print(self.__dish_name, self.__persons, self.__ingredients)


class Ingredient:

    def __init__(self):
        self.__ingredient_name = ""
        self.__quantity = ""
        self.__measure = ""

    def __repr__(self):
        return self.__ingredient_name

    def set_ingredient_name(self, ingredient_name):
        self.__ingredient_name = ingredient_name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_measure(self, measure):
        self.__measure = measure

    def get_ingredient_name(self):
        return self.__ingredient_name

    def get_quantity(self):
        return self.__quantity

    def get_measure(self):
        return self.__measure


recipes_list = []
dish_list = []

with open("read file with recipes/recipes.txt", encoding='utf-8') as file:
    for str_ in file:
        recipes_list.append(str_)


counter = 0
tmp_name = ""
for element in recipes_list:
    if element == "\n":
        counter = 0
        continue
    elif counter == 0:
        dish = Dish()
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
        ingredient = Ingredient()
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
