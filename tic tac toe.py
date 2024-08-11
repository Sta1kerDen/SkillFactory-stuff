field = '''  0 1 2
0 - - -
1 - - -
2 - - -'''

def xturn():
    '''Ход для игрока "x"'''
    global field
    print(field)
    changed = list(field)
    print('''Введите цифру, на координаты которой вы хотите поставить "x":
          1 - 0-0, 2 - 0-1, 3 - 0-2
          4 - 1-0, 5 - 1-1, 6 - 1-2
          7 - 2-0, 8 - 2-1, 9 - 2-2''')
    coord = int(input('''введите цифру: '''))
    if coord == 1:
        if changed[10] == 'x' or changed[10] == 'o':
            print('клетка уже занята')
        else:
            changed[10] = 'x'
    if coord == 2:
        if changed[12] == 'x' or changed[12] == 'o':
            print('клетка уже занята')
        else:
           changed[12] = 'x'
    if coord == 3:
        if changed[14] == 'x' or changed[14] == 'o':
            print('клетка уже занята')
        else:
            changed[14] = 'x'
    if coord == 4:
        if changed[18] == 'x' or changed[18] == 'o':
            print('клетка уже занята')
        else:
            changed[18] = 'x'
    if coord == 5:
        if changed[20] == 'x' or changed[20] == 'o':
            print('клетка уже занята')
        else:
            changed[20] = 'x'
    if coord == 6:
        if changed[22] == 'x' or changed[22] == 'o':
            print('клетка уже занята')
        else:
           changed[22] = 'x'
    if coord == 7:
        if changed[26] == 'x' or changed[26] == 'o':
            print('клетка уже занята')
        else:
            changed[26] = 'x'
    if coord == 8:
        if changed[28] == 'x' or changed[28] == 'o':
            print('клетка уже занята')
        else:
            changed[28] = 'x'
    if coord == 9:
        if changed[30] == 'x' or changed[30] == 'o':
            print('клетка уже занята')
        else:
            changed[30] = 'x'
    field = ''.join(changed)
    print(field)
    print('\n')

def oturn():
    '''Ход для игрока "o"'''
    global field
    print(field)
    changed = list(field)
    print('''Введите цифру, на координаты которой вы хотите поставить "o":
          1 - 0-0, 2 - 0-1, 3 - 0-2
          4 - 1-0, 5 - 1-1, 6 - 1-2
          7 - 2-0, 8 - 2-1, 9 - 2-2''')
    coord = int(input('''введите цифру: '''))
    if coord == 1:
        if changed[10] == 'x' or changed[10] == 'o':
            print('клетка уже занята')
        else:
            changed[10] = 'o'
    if coord == 2:
        if changed[12] == 'x' or changed[12] == 'o':
            print('клетка уже занята')
        else:
           changed[12] = 'o'
    if coord == 3:
        if changed[14] == 'x' or changed[14] == 'o':
            print('клетка уже занята')
        else:
            changed[14] = 'o'
    if coord == 4:
        if changed[18] == 'x' or changed[18] == 'o':
            print('клетка уже занята')
        else:
            changed[18] = 'o'
    if coord == 5:
        if changed[20] == 'x' or changed[20] == 'o':
            print('клетка уже занята')
        else:
            changed[20] = 'o'
    if coord == 6:
        if changed[22] == 'x' or changed[22] == 'o':
            print('клетка уже занята')
        else:
           changed[22] = 'o'
    if coord == 7:
        if changed[26] == 'x' or changed[26] == 'o':
            print('клетка уже занята')
        else:
            changed[26] = 'o'
    if coord == 8:
        if changed[28] == 'x' or changed[28] == 'o':
            print('клетка уже занята')
        else:
            changed[28] = 'o'
    if coord == 9:
        if changed[30] == 'x' or changed[30] == 'o':
            print('клетка уже занята')
        else:
            changed[30] = 'o'
    field = ''.join(changed)
    print(field)
    print('\n')

def owin():
    '''Проверяет соблюдены ли условия для победы o'''
    first = field[10], field[12], field[14]
    second = field[18], field[20], field[22]
    third = field[26], field[28], field[30]
    forth = field[10], field[20], field[30]
    fifth = field[14], field[20], field[26]
    sixth = field[10], field[18], field[26]
    seventh = field[12], field[20], field[28]
    eighth = field[14], field[22], field[30]

    list_of_cond = (first, second, third, forth, fifth, sixth, seventh, eighth)
    for i in list_of_cond:
        if ''.join(i) == 'ooo':
            return True

def xwin():
    '''Проверяет соблюдены ли условия для победы x или o'''
    first = field[10], field[12], field[14]
    second = field[18], field[20], field[22]
    third = field[26], field[28], field[30]
    forth = field[10], field[20], field[30]
    fifth = field[14], field[20], field[26]
    sixth = field[10], field[18], field[26]
    seventh = field[12], field[20], field[28]
    eighth = field[14], field[22], field[30]

    list_of_cond = (first, second, third, forth, fifth, sixth, seventh, eighth)
    for i in list_of_cond:
        if ''.join(i) == 'xxx':
            return True

def renew():
    '''Обновляет поле для повторной игры'''
    global field
    field = '''  0 1 2
0 - - -
1 - - -
2 - - -'''


def tic_tac_toe():
    xturn()
    oturn()
    if xwin() is True:
        print('"x" победили!!!')
        renew()
    if owin() is True:
        print('"o" победили!!!')
        renew()
    if '-' not in field:
        print("Ничья!")
        renew()
    else:
        tic_tac_toe()

tic_tac_toe()