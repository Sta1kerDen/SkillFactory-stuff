A = input('Введите число: ')
B = str(A)
if B == B[::-1]:
    print(A, "- палиндром")
else:
    print(A, "- не палиндром")