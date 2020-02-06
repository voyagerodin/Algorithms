# ==================================================
#
#    Lection 18.
#    Именованные кортежи
#
# ==================================================

from collections import namedtuple
point = namedtuple("point", "x, y, z")
A = point(1, 0, 3)
print(A.x)
print(A.y)
print(A.z)
