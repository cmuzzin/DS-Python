def print_items(n):
    #O(n^2)
    for i in range(n):
        for j in range(n):\
            print(i,j)
    #O(n)
    for k in range(n):
        print(k)


print_items(10) 