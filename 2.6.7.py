try:
    A = int(input('Введите число: '))
except ValueError as e:
    print('Вы ввели неверное число')
else:
    print(f'вы ввели число: {A}')
finally:
    print('Мы на выходе')