import numpy as np;

twoDArray = np.array([
        [11,15,10,6],
        [10,14,11,5],
        [12,17,12,8],
        [15,18,14,9]
    ])

print(twoDArray)

def accessElements(arr, rowI, colI):
    if(rowI >= len(arr)) and colI >= len(arr[0]):
        print('incorrect')
    else:
        print(arr[rowI][colI])

# accessElements(twoDArray, 1,1)

def traverse2D(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i, j])

# traverse2D(twoDArray)

def search2D(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return "The value is location " + str(i) + " " + str(j)
    return "Not here"

# print(search2D(twoDArray, 9))

newTDArray = np.delete(twoDArray, 1, axis = 0)
print(newTDArray)