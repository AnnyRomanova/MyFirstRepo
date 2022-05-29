def read_file(user_file):
    recipes_list = []
    with open(user_file, encoding='utf-8') as file:
        for str_ in file:
            recipes_list.append(str_)
    return recipes_list