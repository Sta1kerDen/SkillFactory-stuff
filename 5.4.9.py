def min_value(M):
    if len(M) == 1:
        return M[0]
    return M[0] if M[0] < min_value(M[1:]) else min_value(M[1:])

M = (5,6,2,1)

print(min_value(M))