# list_a = [1, 2020, 70]
# list_b = [2, 4, 7, 2000]
# list_c = [3, 70, 7]
#
# for a in list_a:
#     for b in list_b:
#         for c in list_c:
#             if a + b + c == 2077:
#                 print(a, b, c)

# OR:

from itertools import product


list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)
