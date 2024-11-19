def read_cook_book(file_name):
    cook_book = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                dish_name = lines[i].strip()
                num_ingredients = int(lines[i + 1].strip())
                ingredients = []
                for j in range(num_ingredients):
                    ingredient_line = lines[i + 2 + j].strip()
                    if not ingredient_line:
                        break
                    ingredient_name, quantity, measure = ingredient_line.split(' | ')
                    ingredients.append({
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })
                cook_book[dish_name] = ingredients
                i += 2 + num_ingredients + 1
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return {}
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return {}

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list


def print_shop_list(shop_list):
    print("{")
    for ingredient, details in shop_list.items():
        print(f"  '{ingredient}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}},")
    print("}")


def main():
    file_name = 'recipes.txt'
    cook_book = read_cook_book(file_name)

    if not cook_book:
        return

    dishes_to_cook = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)

    print_shop_list(shop_list)


if __name__ == '__main__':
    main()