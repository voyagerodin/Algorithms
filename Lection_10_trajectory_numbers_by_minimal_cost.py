# ==================================================
#
#   Lection 10.
#   Count minimal cost of reaching a target cell.
#   asymptotics: O(N)
#
# ==================================================

def count_minimum_cost(N, price: list):
    ''' Count the minimal cost of reaching
        a target cell, if each cell on number line
        has a price for presence it'''

    """ суть алгорима - циклическое суммирование двух стоимостей достижения дискретных позиций
        на числовой прямой - текущей и минимальной их двух предшествующих """

    """ Создание (подготовка) списка с первыми тремя известными элементами и нулевыми
        оставшимися """
    Cost = [float("-inf"), price[1], price[1] + price[2]] + [0] * (N - 3)

    """ сам цикл - это второстепенная часть алгоритма. Сама суть отражается в теле цикла"""
    for i in range(3, N):
        """ Подсчет стоимости достижения текущей позиции - основная часть алгоритма """
        Cost[i] = price[i] + min(Cost[i-1], Cost[i-2])
    return Cost[N-1]

price = [float("-inf"), 4, 3, 2, 5, 6, 4, 3, 2, 1]
print(count_minimum_cost(6, price))
