test_matrix = [[1, 2, 3], 
               [7, -1, 2],
               [123, 2, -1]]
max = test_matrix[0][0]
for row in test_matrix:
    for number in row:
        if number > max:
            max = number
print(max)