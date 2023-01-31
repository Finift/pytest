# башни: с 1 на 3. вводим только n - количество дисков.
def move(n, i, k):
    if n == 1:
        print(n, i, k)
    else:
        tmp = 6 - i - k
        move(n - 1, i, tmp)
        print(n, i, k)
        move(n - 1, tmp, k)


n = int(input())
move(n, 1, 3)
