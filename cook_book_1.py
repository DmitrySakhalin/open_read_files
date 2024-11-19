def read_cook_book(file_name):
    cook_book = {}
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
    return cook_book

def main():
    file_name = 'recipes.txt'
    cook_book = read_cook_book(file_name)
    print("cook_book = {")
    for dish, ingredients in cook_book.items():
        print(f"  '{dish}': [")
        for ingredient in ingredients:
            print(f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, 'measure': '{ingredient['measure']}'}}," )
        print("  ],")
    print("}")

if __name__ == '__main__':
    main()