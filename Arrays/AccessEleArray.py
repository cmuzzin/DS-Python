import array

arr = array.array('i', [1,2,3,4,5,6]) #O(n)
print(arr)

def accessElement(array, index):
    if index > len(array): #O(1)
        print('There is not any element at this index') #O(1)
    else:
        print(array[index]) #O(1)

accessElement(arr, 4)