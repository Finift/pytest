# Петя перешёл в другую школу. На уроке физкультуры ему
# понадобилось определить своё место в строю.Помогите ему это сделать.
# Формат ввода
# Программа получает на вход невозрастающую последовательность
# натуральных чисел,означающих рост каждого человека в строю.
# После этого вводится число X – рост Пети.Все числа во входных
# данных натуральные и не превышают 200.
# Формат вывода
# Выведите номер, под которым Петя должен встать в строй.
# Если в строю есть люди с одинаковым ростом,таким же, как у Пети,
# то он должен встать после них.
def petya_v_sherenge(vse, petya):
    vse.sort(reverse=True)
    if vse[0] > 200 or petya > 200:
        return "Input error: too big value. Please, change it to value <= 200"
    if len(vse) == 0 or petya > vse[0]:
        return 1
    elif petya < vse[len(vse) - 1] or\
            (len(vse) == 1 and petya == vse[0]):
        return len(vse) + 1
    else:
        for i in range(len(vse)):
            if vse[i] >= petya:
                i += 1
            else:
                vse.insert(i, petya)
                return i + 1


vse = input().split()
# vse = [198]
vse = list(map(int, vse))
# petya = 198
petya = int(input())
print(petya_v_sherenge(vse, petya))

