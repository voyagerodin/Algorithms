def fixtureMakeSortedHeap6elements():
    listIn = [15, 8, 11, 3, 0, 9]
    listEtalon = [[0, 3, 9, 15, 8, 11],
                  [0, 8, 3, 15, 9, 11],
                  [0, 3, 8, 15, 11, 9],
                  [0, 9, 3, 15, 11, 8],
                  [0, 3, 8, 15, 9, 11],
                  [0, 8, 3, 15, 11, 9],
                  [0, 3, 9, 11, 8, 15],
                  [0, 8, 3, 11, 9, 15],
                  [0, 3, 8, 11, 15, 9],
                  [0, 3, 8, 11, 9, 15],
                  [0, 9, 3, 11, 15, 8],
                  [0, 8, 3, 11, 15, 9],
                  [0, 3, 9, 8, 11, 15],
                  [0, 3, 11, 8, 9, 15],
                  [0, 8, 3, 9, 11, 15],
                  [0, 3, 11, 9, 8, 15],
                  [0, 3, 9, 8, 15, 11],
                  [0, 8, 3, 9, 15, 11],
                  [0, 3, 8, 9, 15, 11],
                  [0, 3, 8, 9, 11, 15]]

    return listIn, [0, 3, 9, 15, 8, 11] or [0, 8, 3, 15, 9, 11] or [0, 3, 8, 15, 11, 9] or [0, 9, 3, 15, 11, 8]


def fixtureMakeSortedHeap10elements():
    listIn = [66, 1, 7, 1, 10, 22, 6, 29, 83, 2]
    listEtalon = [1, 1, 6, 29, 2, 22, 7, 66, 83, 10]
    return listIn, listEtalon
