def print_2_add_2():
    C = 2+2
    print(C)


def hello_world():
    print('Hello World')


def delit(a, n):
    if a % n == 0:
        print(f'число {n} является делителем числа {a}')
    else:
        print(f'число {n} не является делителем числа {a}')

def stairs(n):
    for i in range(n, 0, -1):
        print('*' * i)
 

def multipliers(k):
    mult = 0
    for j in range(1, k+1):
        if k % j == 0:
            mult += 1
    print(f'Количестов делителей числа {k}: {mult}')


def check_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        return True
    else:
        return False


def check(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False
Text = check('Кит на море не романтик')
print(Text)