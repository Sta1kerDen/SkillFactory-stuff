def nested_list_contains(nested_list, target):
    counter = 0
    for item in nested_list:
        if item == target:
            counter += 1
        elif isinstance(item, list):
            if nested_list_contains(item, target):
                counter += 1
    return counter


my_list = [1, 2, [4, 8, [2, 0]], 2, 8, [5, 7]]
check = nested_list_contains(my_list, 8)
print(check)