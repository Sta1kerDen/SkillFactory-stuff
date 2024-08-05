def counter(x):
    def inner(y):
        return x + y
    x += 1
    return inner


my_counter = counter(1)

print(my_counter(1))
print(my_counter(1))
print(my_counter(1))