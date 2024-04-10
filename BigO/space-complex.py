def sum(n):
    print(n)
    if (n <= 0):
        return 0
    return n + sum(n-1)

#O(1) since pair sum is not added into the stack
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i +1)
    print(total)

def pair_sum(a, b):
    return a + b

pair_sum_sequence(5)