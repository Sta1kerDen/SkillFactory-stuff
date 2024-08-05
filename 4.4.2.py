def list_repeater(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value

for i in list_repeater:
    print (i)
