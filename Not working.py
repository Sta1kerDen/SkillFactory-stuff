def outer():
    funcs = []
    for i in range(4):
        funcs.append(i)
        print(funcs)


outer()

# результатом должен быть список от 0 до 3, или же нужно как-то вызвать конкретную цифру по порядку из outer: outer()[0]() не работает (такой вариант был на вебинаре)

#починено, но до этого вариант выглядел так:

def outer():
    funcs = []
    for i in range(4):
        def func(a=i):
            print(a)
            funcs.append(func)
        print(funcs)