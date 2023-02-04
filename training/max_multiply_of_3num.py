# В данном списке из n≤10⁵ целых чисел найдите три числа,
# произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# То есть сортировку использовать нельзя.
# Выведите три искомых числа в любом порядке.
from heapq import nlargest, nsmallest


def max_multiply_of_3num(lst):
    positive, negative = [], []
    multipliers = []
    if len(lst) > 10 ** 5:
        return 'Error. List is too big'
    else:
        if len(lst) == 3:
            return lst
        else:
            for i in range(len(lst)):
                if lst[i] >= 0:
                    positive.append(lst[i])
                elif lst[i] < 0:
                    negative.append(lst[i])
            mult_pos = nlargest(3, positive)
            mult_neg = nsmallest(3, negative)
            if len(negative) <= 1:
                return mult_pos
            elif len(positive) < 1:
                return nlargest(3, negative)
            else:
                res = []
                mult = []
                m_dict = {}
                for i in range(len(mult_pos)):
                    for j in range(len(mult_neg) - 1):
                        result = mult_pos[i] * mult_neg[j] * mult_neg[j + 1]
                        res.append(result)
                        mult.append([mult_pos[i], mult_neg[j], mult_neg[j + 1]])
                        j += 1

                    result = mult_pos[i] * mult_neg[0] * mult_neg[2]
                    res.append(result)
                    mult.append([mult_pos[i], mult_neg[0], mult_neg[2]])
                    m_dict = dict(zip(res, mult))
                    i += 1
                if len(mult_pos) >= 3:
                    result = mult_pos[0] * mult_pos[1] * mult_pos[2]
                    res.append(result)
                    mult.append([mult_pos[0], mult_pos[1], mult_pos[2]])
                    m_dict[result] = [mult_pos[0], mult_pos[1], mult_pos[2]]
                answ = max(res)
                return m_dict[answ]


lst = list(map(int, input().split()))
print(*max_multiply_of_3num(lst))
