L = [ a for a in some_iter_obj if cond ] # Это равно следующему:

L = []
for a in some_iter_obj:
    if cond:
        L.append(a)

M = [[i * j for j in range(1,11)] for i in range (1,11)]
print(M)




L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1

B = [a*b for a,b in zip(L, M)]


print(B)