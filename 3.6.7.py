n = 2
s = 2
b = s**n
while b < 10000:
    n += 1
    b = s**n
print(b)
print(n-1)