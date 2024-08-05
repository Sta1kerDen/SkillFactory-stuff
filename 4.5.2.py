def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f"Функция {func} была вызвана {count} раз")
    return wrapper

@counter
def say_word(word):
   print(word)

say_word('A')
say_word('A')
say_word('A')