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