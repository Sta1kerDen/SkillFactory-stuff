A = 406587234239
while A % 10 != 5:
    if A <= 0:
        break
    A = A // 10
print(A % 10 == 5)