from Study.decorators import measure_time
import math


# def factorial(n):
#     fact = n
#     if n == 0:
#         return 1
#     else:
#         for i in range(1, (n - 1)):
#             fact = fact * (n - i)
#         return fact
#
#
# n = int(input())
# start = datetime.now()
# print(factorial(n))
# end = datetime.now()
# print((end - start).total_seconds() * 10**3)

# В два раза быстрее, но n до 998!
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# n = int(input())
# start = datetime.now()
# print(factorial(n))
# end = datetime.now()
# print((end - start).total_seconds() * 10**3)


# вариант с декоратором для разнообразия:
@measure_time
def factorial(n):
    print(math.factorial(n))


factorial(110)
