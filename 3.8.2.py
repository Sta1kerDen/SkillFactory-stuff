test_matrix = [[1, 2, 3],
              [7, -1, 2],
              [123, 2, -1]]
lines = len(test_matrix)
number = 0
for line in test_matrix:
    if len(line) == lines:
        number += 1
print(number == lines)