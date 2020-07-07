def read_cook_book_from_file(filename):
    dishes = {}
    with open(filename, encoding='utf-8') as cb_file:
        while 'true':
            dish_name = cb_file.readline()
            if len(dish_name) == 0:
                break

            dish_name = dish_name.strip()
            if len(dish_name) == 0:
                continue
                
            ingredients_count = int(cb_file.readline())
            cur_ingredient = 0
            ingredients = list()
            while cur_ingredient < ingredients_count:
                ingredient_desc = cb_file.readline().strip()
                ingredient_parts = ingredient_desc.split(sep='|')
                ingredient_info = {
                    'ingredient_name': ingredient_parts[0],
                    'quantity': int(ingredient_parts[1]),
                    'measure': ingredient_parts[2]
                }
                ingredients.append(ingredient_info)
                cur_ingredient += 1

            dishes[dish_name] = ingredients
            
    return dishes


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    def ingredients_by_portions(inredient_info):
        ingredient_info['quantity'] *= person_count
        return ingredient_info

    shop_list = dict()
    for dish in dishes:
        dish_ingredients = cook_book.get(dish)
        if dish_ingredients == None:
            continue
               
        for ingredient_info in dish_ingredients:
            ingredient_name = ingredient_info['ingredient_name']
            if shop_list.get(ingredient_name) == None:
                shop_list[ingredient_name] = {
                    'quantity': ingredient_info['quantity'] * person_count,
                    'measure': ingredient_info['measure']
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient_info['quantity'] * person_count

    return shop_list

cook_book = read_cook_book_from_file("recipes.txt")

shop_list = get_shop_list_by_dishes(cook_book, ['Омлет','Фахитос'], 2)
print(shop_list)

