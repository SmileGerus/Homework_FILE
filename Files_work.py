from pprint import pprint
def get_shop_list_by_dishes(dishes: list, person_count: int, book):
    ingredients = {}
    new_ingredient = 0
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                new_ingredient = ingredient['quantity'] * person_count + \
                                         ingredients[ingredient['ingredient_name']]['quantity']
            else:
                new_ingredient = ingredient['quantity'] * person_count
            ingredients[ingredient['ingredient_name']] = \
                {'measure': ingredient['measure'],
                 'quantity': new_ingredient}
    pprint(ingredients)

def create_cook_book(file, cou):
    for j in range(cou):
        dish = file.readline().strip()
        count_ing = file.readline().strip()
        ingredients = []
        for i in range(int(count_ing)):
            data = file.readline().strip().split('|')
            ingredients_dict = {
                "ingredient_name": data[0].strip(),
                "quantity": int(data[1]),
                "measure": data[2].strip()
            }
            ingredients.append(ingredients_dict)
        cook_book[dish] = ingredients
        file.readline()


cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as f:
    cou = 1
    for string in f.readlines():
        if string.strip().split() == []:
            cou += 1

with open('recipes.txt', 'r', encoding='utf-8') as f:
    create_cook_book(f, cou)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2, cook_book)



