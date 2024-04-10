import array

my_array = array.array('i', [1,2,3,4]) #O(n)
print(my_array)
my_array.insert(5, 6) #O(n) worst case
print(my_array)