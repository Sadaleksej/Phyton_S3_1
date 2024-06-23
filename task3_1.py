def remove_duplicates(input_list):
    unique_list = []
    duplicates_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
        else:
            duplicates_list.append(item)
    return unique_list, duplicates_list


input_list = [1, 2, 2, 3, 3, 4, 5, 5, 7, 8, 9, 8, 11]
result_list, res_dup = remove_duplicates(input_list)
print("Исходный список:", input_list)
print("Список с уникальными элементами:", result_list)
print("Список дубликатов: ", res_dup)
