# ==================================================
#
#    Lection 19.
#    Heap structure
#
# ==================================================

class HeapStructure:
    def __init__(self):
        self.val = []
        self.size = 0

    def clean(self):
        self.val = []
        self.size = 0

    def insert(self, x):
        self.val.append(x)
        self.size += 1
        self.siftUp(self.size-1)

    def delete(self, n):
        self.val[n], self.val[self.size-1] = self.val[self.size-1], self.val[n]
        self.val.pop()
        self.size -= 1
        self.siftDown(n)

    def siftDown(self, i):
        while (2*i + 1) < (self.size - 1) and (2*i + 2) < (self.size - 1) and self.val[i] > self.val[2*i + 1] and self.val[i] > self.val[2*i + 2]:

            if self.val[i] > self.val[2*i + 1]:
                self.val[i], self.val[2*i + 1] = self.val[2*i + 1], self.val[i]
                i = 2*i + 1
            elif self.val[i] > self.val[2*i + 2]:
                self.val[i], self.val[2*i + 2] = self.val[2*i + 2], self.val[i]
                i = 2*i + 2

    def siftUp(self, i):
        while i != 0 and self.val[i] < self.val[(i-1) // 2]:
            self.val[i], self.val[(i-1) // 2] = self.val[(i-1) // 2], self.val[i]
            i = (i-1) // 2

    def insertList(self, L):
        for item in L:
            self.val.append(item)
            self.size += 1
            self.siftUp(self.size-1)

    def show(self):
        print(self.val)

    def get(self):
        return self.val


listIn0 = [15, 8, 11, 3, 0, 9]
listIn1 = [6, 3, 4, 7, 2, 5]
listIn3 = [36, 27, 12, 43, 55, 11, 29, 88, 30, 44, 77, 66]

heap = HeapStructure()
print(listIn3)
heap.insertList(listIn3)
heap.show()
# heap.insert(1)
heap.delete(6)

heap.show()
