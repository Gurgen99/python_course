  def f(n):
       if n == 1:
            return 1
        return n * f(n-1)


r = f(7)
print(r)

# 1 1 2 3 5 8 13 21 34


def fibonacci(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


k = fibonacci(10)
print(k)