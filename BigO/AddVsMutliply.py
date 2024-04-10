def print_items(a,b):
    #O(a)
    for i in range(a):
        print(i)
    #O(b)
    for j in range(b):
        print(j)

#together / on top of each other: O(a+b)

#nested loop:  O(a * b)

print_items(1,2) 