import unittest
import generate.generateHeap
import generate.generatePermutations
from fixtureHeap import fixtureHeap as FX
from modules.heapStructure import HeapStructure


class myTestMerge(unittest.TestCase):

    def test_checkSortListToHeap6elements(self):
        listIn, listEtalon = FX.fixtureMakeSortedHeap6elements()
        heap = HeapStructure()
        heap.insertList(listIn)
        listResult = heap.get()
        self.assertEqual(listResult, listEtalon)

    def test_checkSortListToHeap10elements(self):
        listIn, listEtalon = FX.fixtureMakeSortedHeap10elements()
        heap = HeapStructure()
        heap.insertList(listIn)
        listResult = heap.get()
        self.assertEqual(listResult, listEtalon)


if __name__ == '__main__':
    unittest.main()

# comment
# comment-2
