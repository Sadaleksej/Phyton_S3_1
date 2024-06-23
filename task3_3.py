def find_combinations(items, max_weight):

    def find_combinations_helper(items, max_weight, current_items, current_weight, index):
        if current_weight > max_weight:
            return

        if index == len(items):
            combinations.append(current_items)
            return

        find_combinations_helper(items, max_weight, current_items.copy(), current_weight, index + 1)
        find_combinations_helper(items, max_weight, current_items + [items[index]], current_weight + items[index][1], index + 1)

    combinations = []
    find_combinations_helper(items, max_weight, [], 0, 0)

    return combinations


items = {
    "Книга": 1,
    "Лэптоп": 4,
    "Консервы": 1,
    "Котелок": 8,
    "Фотоаппарат": 2,
    "Вода": 3
}
max_weight = 15

possible_combinations = find_combinations(list(items.items()), max_weight)
for combination in possible_combinations:
    print("Вариант компановки рюкзака: ", combination)

