random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]
max = random_matrix[0][0]
for row in random_matrix:
   for el in row:
      if el > max:
           max = el
print(max)