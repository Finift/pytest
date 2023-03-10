# Теорема Лагранжа утверждает, что любое натуральное число можно представить в виде суммы четырех точных квадратов. По данному числу n найдите такое представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число.
# Формат ввода
# Программа получает на вход одно натуральное число n < 10000.
# Формат вывода
# Программа должна вывести от 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число.
# Стоит протестить: 27, 29, 30, 32, 48


def lagrange(n):
    if n >= 10000:
        return 'input error'
    else:
        nw = n
        answ = []
        sc = int((n ** 0.5) // 1)
        if sc ** 2 == n:
            answ.append(sc)
            return answ
        else:
            for i in range(sc):
                c = sc - i
                k = 0
                n = nw
                answ = [c]
                while k < 3:
                    k += 1
                    n = n - (c ** 2)
                    c = int((n ** 0.5) // 1)
                    answ.append(c)
                    if c ** 2 == n:
                        return answ


n = int(input())
print(*lagrange(n))
