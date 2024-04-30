def fibbonacci(n):
    assert n >= 0 and int(n) == n, "Must be positive int only"
    if n == 1 or n ==0:
        return n
    #f(n) = f(n-1) + f(n-2);
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)
    
print(fibbonacci(8))