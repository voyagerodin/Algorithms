# ==================================================
#
#    Lection 17.
#    Packing backpack!
#    Укладка дискретного конечного рюкзака.
#    Каждый предмет обладает массой и стоимостью.
#    asymptotics: O(N*M)
#
# ==================================================

""" Алгоритм определяет такой набор из элементов списка (назовем его - список масс предметов), что сумма набора не должна превышать определенного заданного числа (назовем его - максимальная масса) и при этом сумма элементов из второго списка (список стоимостей предметов), индексы которых соответствуют индексам элементов из списка масс в этом наборе, была максимальна из всех возможных вариантов наборов """


""" Функция, вычисляющая сумму некоторых элементов списка стоимостей, такую, что она удовлетворяет двум условиям: 
     1)   индексы элементов списка стоимостей, составляющих данную сумму, соответствуют индексам некоторых элементов из списка масс собранных в такой набор, что их сумма не превышает максимальное заданное изначально число (максимальную массу);
     2)   искомая сумма некоторых элементов списка стоимостей максимальна из всех сумм возможных наборов элементов, удовлетворяющих первому условию """
def bestTotalCost(M, C, W):
     
     """ Второстепенная часть. Подготавливаем двумерный массив, номера строк которого соответствуют индексам из списков (масс или стоимостей), а столбцы соответствуют последовательно увеличивающимся на единицу пороговым значениям максимальным (на данной текущей итерации) массам"""
     F = [[0]*(W+1) for i in range(len(M))]

     """ Второстепенная часть. Запускаем циклы перебора по элементам списка масс предметов до последнего включительно, а также по пороговым значениям максимальных масс от нулевой до заданной максимальной массы включительно """
     for i in range(1, len(M)):
          for w in range(1, W + 1):

               """ Основная часть. Здесь мы выбираем, чем заполнить текущую ячейку двумерного массива - либо суммарной стоимостью предыдущего набора предметов (первых i предметов без текущего), в случае если значение элемента из списка масс больше текущего порогового значения максимальной массы (тогда значение текущего элемента списка масс не суммируется с уже набранным набором), либо суммой, состоящей из текущего элемента списка стоимостей и суммарной стоимости предыдущего набора, которая уже посчитана в ячейке двумерного массива в столбце с номером, равным разности текущего порогового значения максимальной массы и значения текущего элемента списка масс - в случае, если значение элемента списка масс не превышает текущего порогового значения максимальной массы """
               if M[i] <= w:
                    F[i][w] = max(F[i-1][w], F[i-1][w-M[i]] + C[i])
               else:
                    F[i][w] = F[i-1][w]
                    
     """ Второстепенная часть. Возвращается кортеж, состоящий из вычисленного двумерного массива суммарных стоимостей, и последнего элемента этого массива """
     return F, F[i][w]

""" Функция, вычисляющая номера тех элементов списка масс, которые принимались в набор и их индексы соответствуют индексам тех элементов списка стоимостей, которые добавлялись к суммам стоимостей в ячейках двумерного массива на строчках с номерами, меньшими на единицу чем добавляемый элемент, и в столбцах с номером, равным разности между номером текущего столбца и значением текущего (добаляемого в набор) элемента списка масс. """
def insideBackpack(F, M, W):

     """ Второстепенная часть. Подготовка исходных данных для вычисления индексов элементов из списка масс, попавших в набор - пустого списка индексов и переменного индекса столбца """
     backpack = []
     tmp = W

     """ Второстепенная часть. Запускает цикл по элементам списка масс от конца к началу. """
     for i in range(len(M)-1, 0, -1):

          """ Основная часть. Включает номер элемента списка масс в список набора элементов, если значение в текущей ячейке больше значения в ячейке строчкой выше, и меняет столбец для следующего рассматриваемого элемента (в следующей итерации цикла) вычитая из номера текущего столбца значение текущего элемента списка масс. """
          if F[i][tmp] != F[i-1][tmp]:
               backpack.append(i)
               tmp -= M[i]

     """ Второстепенная часть. Возвращает ответ функции - список индексов элементов списка масс, составивших набор, сумма которого не превышает заданное пороговое число и сумма элементов списка стоимостей, индексы которых соответствуют индексам элементов в наборе, максимальна. """
     return backpack

thingMass = [0, 7, 3, 1, 5, 4]
thingCost = [0, 10, 4, 2, 6, 7]
backpackMass = 12

bestCost = bestTotalCost(thingMass, thingCost, backpackMass)
print(bestCost[1])
print(insideBackpack(bestCost[0], thingMass, backpackMass))     

               
