def infinite_sequence():
    n=0
    while True:
        yield n
        n += 1


for num in infinite_sequence():
    print(num)
    if num >= 5:
        break