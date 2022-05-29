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