# ==================================================
#
#    Lection 19.
#    Heap structure
#
# ==================================================


class HeapStructure:
    def __init__(self):
        self.values = []
        self.size = 0

    def clean(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.siftUp(self.size-1)

    def delete(self, n):
        self.values[n], self.values[self.size -
                                    1] = self.values[self.size-1], self.values[n]

    def siftUp(self, i):
        while i != 0 and self.values[i] < self.values[(i-1) // 2]:
            self.values[i], self.values[(
                i-1) // 2] = self.values[(i-1) // 2], self.values[i]
            i = (i-1) // 2

    def insertList(self, L):
        for item in L:
            self.values.append(item)
            self.size += 1
            self.siftUp(self.size-1)

    def show(self):
        print(self.values)

    def get(self):
        return self.values


listIn0 = [15, 8, 11, 3, 0, 9]
listIn1 = [6, 3, 4, 1, 2, 5]
listIn3 = [66, 1, 7, 1, 10, 22, 6, 29, 83, 2]

heap = HeapStructure()

heap.insertList(listIn1)
heap.show()
heap.delete(0)
heap.show()
