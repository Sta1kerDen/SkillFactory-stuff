def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


field = [[" "] * 3 for i in range(3)]

def show():
    print()
    print('    | 0 | 1 | 2 |')
    print('    -------------')
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("    -------------")


def ask():
    while True:
        coords = input("Ваш ход: ").split()
        if len(coords) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = coords
        
        if not(x.isdigit() and y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)
        
        if x > 2 or x < 0 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != ' ':
            print('Клетка занята!')
            continue
        else:
            return x, y
        

def xcheck_win():
    
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X', 'X', 'X']:
            print("Победили крестики!")
            return True
        
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X', 'X', 'X']:
            print("Победили крестики!")
            return True
    

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ['X', 'X', 'X']:
        print("Победили крестики!")
        return True
    
    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ['X', 'X', 'X']:
        print("Победили крестики!")
        return True
    

    return False

def ocheck_win():
    
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['O', 'O', 'O']:
            print("Победили нолики!")
            return True
        
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['O', 'O', 'O']:
            print("Победили нолики!")
            return True
    

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ['O', 'O', 'O']:
        print("Победили нолики!")
        return True
    
    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ['O', 'O', 'O']:
        print("Победили нолики!")
        return True
    

    return False

greet()
num = 0
while True:
    num+=1

    show()

    if num % 2 == 1:
        print(' Ходит крестик ')
    else:
        print(' Ходит нолик ')
    
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    
    if xcheck_win() or ocheck_win():
        break

    if num == 9:
        print('Ничья!')
        break