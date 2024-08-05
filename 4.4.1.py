def nat(n = None):
    if n == None:
        n = 1
    yield n

    while True:
        n = n + 1
        yield n

# OR

def count(start = 1, step = 1):
    counter = 1
    while True:
        yield counter
        counter += step
