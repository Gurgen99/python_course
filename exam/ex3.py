def ex3(n):
    a = n % 10
    b = n // 10 %10
    c = a*b
    return c
print(ex3(366))