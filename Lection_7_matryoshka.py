def matryoshka(n):
''' МАТРЕШКА '''

    if n == 1:
        print("Матрешечка !!!")
    else:
        print(" верх матрёшки №", n)
        matryoshka(n - 1)
        print(" низ матрёшки №", n)


matryoshka(5)
