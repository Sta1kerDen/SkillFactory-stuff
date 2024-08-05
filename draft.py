def outer():
    funcs = []
    for i in range(4):
        def func(a=i):
            print(a)
            funcs.append(func)
        print(funcs)


outer()