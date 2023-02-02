# def reverse(A):
#     if len(A) == 1:
#         answ.append(*A)
#         return answ
#     else:
#         for i in range((len(A) - 1), 0, -1):
#             answ.append(A[i])
#
#         answ.append(A[0])
#         return answ
#
#
# A = list(map(int, input().split()))
# answ = []
# print(*reverse(A))
#
# # или
#
B = input().split()
B.reverse()
print(*B)

#или

# C = str(input())
# print(C[::-1])