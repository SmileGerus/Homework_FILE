from pprint import pprint
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
    print(cook_book)





