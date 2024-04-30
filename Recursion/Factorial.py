def factorial(n):
    print (n)
    assert n >= 0 and int(n) == n, "Must be positive int only"
    if n == 1 or n ==0:
        return 1
    else:
        return n * factorial(n -1)

# factorial(10)
print(factorial(10))