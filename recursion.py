def nested_list_contains(nested_list, target):
    for item in nested_list:
        if item == target:
            return True #как только он найдёт цель - он тут же остановится и не будет проверять дальше
        elif isinstance(item, list):
            if nested_list_contains(item, target): #вызываем снова корневую функцию, если наш item является списком
                return True
    return False

my_list = [1, 2, [4, 8, [2, 0]], 2, 9, [5, 7]]
check = nested_list_contains(my_list, 8)
print(check)