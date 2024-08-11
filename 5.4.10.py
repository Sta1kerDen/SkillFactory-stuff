def mirror(M, res = 0):
    if M:
        return mirror(M // 10, res*10 + M%10)
    else:
        return res

print(mirror(12345))