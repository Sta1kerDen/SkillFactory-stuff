L = list(map(int, input().split()))
L[0], L[-1] = L[-1], L[0]
L.append(sum(L))
print(L)