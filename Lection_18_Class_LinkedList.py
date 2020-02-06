# ==================================================
#
#    Lection 18.
#    Класс "Связанный массив"
#    asymptotics: O(1)
#
# ==================================================

class LinkedList:
     def __init__(self):
          self._begin = None
     def insert(self, x):
          self._begin = [x, self._begin]
     def pop(self):
          assert self._begin is not None, "List is empty"
          x = self._begin[0]
          self._begin = self._begin[1]
          return x

a = LinkedList()

for i in range(1, 100, 1):
     a.insert(i)

print(a.pop())

N = 10000
A = [0] * N
A.insert(0, 1)
print(A)

