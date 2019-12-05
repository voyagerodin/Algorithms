#==================================================
#
#   Lection 10.
#   Binary search.
#   asymptotics: O(log(N))
#
#==================================================


def leftBound(A, key):
    ''' left bound points to the element, preceding the desired '''
    left = -1
    right = len(A)

    while (right - left) > 1:
        middle = (left + right) // 2
        if A[middle] < key:             # this is MAIN PART
            left = middle               # because here occure
        else:                           # distribution and choise -
            right = middle              # which side will be drop.

    return left


def rightBound(A, key):
    ''' Right bound points to the next element after the desired '''
    left = -1
    right = len(A)

    while (right - left) > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


A = sorted([1, 3, 2, 5, 4, 4, 4, 8, 12])

print(leftBound(A, 6))
print(rightBound(A, 6))
