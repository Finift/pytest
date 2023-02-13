from _datetime import datetime

# def factorial(n):
#     fact = n
#     for i in range(1, (n - 1)):
#         fact = fact * (n - i)
#     return fact
#
#
# n = int(input())
# start = datetime.now()
# print(factorial(n))
# end = datetime.now()
# print((end - start).total_seconds() * 10**3)

# В два раза быстрее, но n до 996!
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
start = datetime.now()
print(factorial(n))
end = datetime.now()
print((end - start).total_seconds() * 10**3)
