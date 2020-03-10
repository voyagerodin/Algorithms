# ==================================================
#
#    Lection 19.
#    Heap structure
#
# ==================================================
from modules.heapStructure import HeapStructure as HS
import generate.generatePermutations as GP

listIn0 = [15, 8, 11, 3, 0, 9]
listIn1 = [6, 3, 4, 1, 2, 5]
listIn3 = [66, 1, 7, 1, 10, 22, 6, 29, 83, 2]

listIndexPermutations = []
heap = HS()
listHeapPermutation = []

# GP.generateIndexPermutations(
#     len(listIn3), len(listIn3), listIndexPermutations)

# listOut = GP.generateListInPermutations(listIn3)

# for item in listOut:
#     heap.insertList(item)
#     if heap.get() not in listHeapPermutation:
#         listHeapPermutation.append(heap.get())
#     heap.clean()

# for item in listHeapPermutation:
#     print(item)

heap.insertList(listIn1)
heap.show()
