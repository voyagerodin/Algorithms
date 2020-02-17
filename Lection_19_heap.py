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

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size-1)

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i-1) // 2]:
            self.values[i], self.values[(i-1) // 2] = self.values[(i-1) // 2], self.values[i]
            i = (i-1) // 2

    def show(self):
        print(self.values)


heap = HeapStructure()
heap.insert(17)
heap.insert(5)
heap.insert(7)
heap.insert(1)
# heap.insert(10)

heap.show()