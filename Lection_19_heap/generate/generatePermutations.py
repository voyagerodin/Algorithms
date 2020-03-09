listIndexPermutations = []


def finds(number, A):
    """ Ищет number в A и возвращает
            True - если такой есть,
            False - если такого нет.
    """""
    for xx in A:
        if number == xx:
            return True
    return False


def generateIndexPermutations(N: int, M: int = -1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях
        с префиксом prefix
    """
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []

    """ 
    Второстепеная часть. Создает отдельный вспомогательный список с элементами,
    равными элементам списка префикса для того, чтобы в список всех перестановок 
    помещались не ссылки на элементы префикса, а независимые от изменяемого префикса 
    объекты, что позволит сохранять и накапливать элементы в списке перестановок при периодическом
    изменении элементов префикса."""
    arr = []
    if M == 0:
        for item in prefix:
            arr.append(item)
        listIndexPermutations.append(arr)
        return

    for numbers in range(1, N + 1):
        if finds(numbers, prefix):
            continue
        prefix.append(numbers)
        generateIndexPermutations(N, M - 1, prefix)
        prefix.pop()


def generateListInPermutations(listIn):
    listOut = []

    for item in listIndexPermutations:
        listOut.append(item)

    for i in range(len(listIndexPermutations)):
        j = 0
        for index in listIndexPermutations[i]:
            listOut[i][j] = listIn[index-1]
            j += 1

    return listOut