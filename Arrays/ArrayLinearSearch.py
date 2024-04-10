import array

arr = array.array('i', [1,2,3,4,5,6]) #O(n)

def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1  

print(linearSearch(arr, 3))