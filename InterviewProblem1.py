matrix = [[1,4,7,11,15],
         [2,5,8,12,19],
         [3,6,9,16,22],
         [10,13,14,17,24],
         [18,21,23,26,30]]

# For the above matrix, write an algorithm to search an element with a time complexity of O(n)

# print(matrix[0][0])

def Search2D_SortedMatrixSearch(matrix,element):
    i = 0
    j = len(matrix[0]) - 1
    n = len(matrix)

    while (i < n and j >= 0 ):
        if matrix[i][j] == element:
            return True
        elif matrix[i][j] < element:
            i += 1
        else:
            j -= 1
    return False


result = Search2D_SortedMatrixSearch(matrix,30)
print(result)