import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def findNum(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i, array[i])

findNum(myArray, 8)