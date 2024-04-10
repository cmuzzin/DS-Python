import array

array1 = array.array('i', [1,2,3,4]) #O(n)
array2 = array.array('d', [1.3,1.5,1.6]) #O(n)
print(array1)

def traverseArray(array):
    for i in array: #O(n)
        print(i) #O(1)

traverseArray(array1)