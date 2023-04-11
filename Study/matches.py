# Вдоль прямой выложены три спички. Необходимо переложить одну из них так,
# чтобы при поджигании любой спички сгорали все три.
# Для того чтобы огонь переходил с одной спички на другую,
# необходимо чтобы эти спички соприкасались (хотя бы концами).
# Требуется написать программу, определяющую,какую из трех спичек необходимо переместить.
# Вводятся шесть целых чисел: l₁,r₁,l₂,r₂,l₃,r₃– координаты первой,второй и третьей спичек соответственно (0≤lᵢ<rᵢ≤100).
# Каждая спичка описывается координатами левого и правого концов по горизонтальной оси OX.
# Выведите номер искомой спички. Если возможных ответов несколько,
# то выведите наименьший из них (наименьший по номеру спички). В случае,
# когда нет необходимости перемещать какую-либо спичку, выведите 0.
# Если же требуемого результата достигнуть невозможно, то выведите -1.
# спички могут иметь разную длин, спички могут лежать в любом порядке.
from Study.decorators import timer


@timer
def matches(l1, r1, l2, r2, l3, r3):
    # Вычислим длины спичек:
    ln1 = r1-l1
    ln2 = r2-l2
    ln3 = r3-l3
    # Вычислим минимальные расстояния между спичками:
    minln12 = min(abs(l2 - r1), abs(l1 - r2))
    minln23 = min(abs(l3 - r2), abs(l2 - r3))
    minln13 = min(abs(l3 - r1), abs(l1 - r3))
    if 0 <= l1 < r1 <= 100 and 0 <= l2 < r2 <= 100 and 0 <= l3 < r3 <= 100:
        # Если спички 1 и 2 пересекаются:
        if l1 <= r2 and l2 <= r1:
            if (l3 <= r2 and l2 <= r3) or (l3 <= r1 and l1 <= r3):
                return 0  # пересекаются все три спички
            elif minln23 > ln1 and minln13 > ln2:
                return 3  # расстояние до спички 3 больше чем длина 1 или 2
            elif minln23 > ln1 and minln13 <= ln2:
                return 2  # расстояние до спички 3 больше чем длина 1, но меньше, чем длина 2
            else:
                return 1
        # Если спички 3 и 2 пересекаются:
        elif l2 <= r3 and l3 <= r2:
            return 1
        # Если спички 1 и 3 пересекаются:
        elif l1 <= r3 and l3 <= r1:
            if minln23 <= ln1:
                return 1
            elif minln12 <= ln3:
                return 3
            else:
                return 2
        # Если спички не пересекаются:
        else:
            if minln23 <= ln1:
                return 1
            elif minln13 <= ln2:
                return 2
            elif minln12 <= ln3:
                return 3
            else:
                return -1
    else:
        return -1


matches(2, 3, 7, 9, 6, 8)
print(matches(2, 3, 7, 9, 6, 8))

