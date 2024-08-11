def divided_by_two(x):
    return x % 2 == 0

result = filter(divided_by_two, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))