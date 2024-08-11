def equal(n,s):
    if s < 0:
        return False
    if n < 10:
        return n == s
    else:
        return equal(n//10, s - n%10)

print(equal(421, 5))