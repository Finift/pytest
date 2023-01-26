n = int(input())

def factorial(n):
    fact = n
    for i in range(1, (n - 1)):
        fact = fact * (n - i)
    return fact
print(factorial(n))
