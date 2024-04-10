def findBiggestNumber(arr):
    biggestNumber = arr[0] #O(1)
    for index in range(1, len(arr)): #O(n)
        if (arr[index] > biggestNumber): #O(1)
            biggestNumber = arr[index] #O(1)
    print(biggestNumber) #O(1)

    #time complex = O(1) + O(n) + O(1) = O(n)

findBiggestNumber([5, 88, 6, 8 ,13, 15, 56, 17, 34])