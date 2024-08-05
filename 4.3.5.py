def nat_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + nat_sum(n // 10)
print(nat_sum(2356))