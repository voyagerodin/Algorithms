def finds(number, A):
    """ Ищет number в A и возвращает 
            True - если такой есть,
            False - если такого нет.  
    """""
    for xx in A:
        if number == xx:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях
        с префиксом prefix  
    """""
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []

    if M == 0:
        print(prefix)
        return

    for numbers in range(1, N + 1):
        if finds(numbers, prefix):
            continue
        prefix.append(numbers)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()

generate_permutations(3, 2)
