# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
def count_different_nums(lst):
    count = 1
    if len(lst) == 0:
        return 0
    else:
        for i in range(len(lst) - 1):
            if lst[i + 1] > lst[i]:
                count += 1
                i += 1
            else:
                i += 1
        return count


lst = list(map(int, input().split()))
print(count_different_nums(lst))
