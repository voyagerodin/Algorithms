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
