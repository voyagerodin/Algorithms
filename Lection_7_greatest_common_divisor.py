""""       Алгоритм Эвклида  """""


def gcdWithDifference(a, b):
    """ поиск НОД с помощью постоянного вычитания бОльшего числа из меньшего"""
    if a == b:
        return a
    elif a > b:
        return gcdWithDifference(a - b, b)
    else:
        return gcdWithDifference(a, b - a)


print(gcdWithDifference(3, 7))


def gcdWithMod(a, b):
    """ поиск НОД с помощью постоянного деления по модулю бОльшего числа на меньшее"""
    if b == 0:
        return a
    else:
        return gcdWithMod(b, a%b)

print(gcdWithMod(6, 154))