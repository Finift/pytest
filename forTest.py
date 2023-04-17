# st = input().split(' ')
# lst = list(map(int, st))
lst_res = []
lst = []


def sqrt_nums(lst):
    for num in lst:
        res = num ** 2
        lst_res.append(res)
    lst_res.sort()
    return lst_res


print(sqrt_nums(lst))
