def diagonal_sum(matrix):
    total = 0
    print(len(matrix))
    for i in range(len(matrix)):
        print(i)
        total += matrix[i][i]
    return total

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))