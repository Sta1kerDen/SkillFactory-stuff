from time import time, sleep

def my_timer(func):
    def wrapper():
        start_time = time()
        func()
        print(f'Время работы функции - {time() - start_time} с.')
    return wrapper


@my_timer
def my_func():
    sleep(3)

my_func()