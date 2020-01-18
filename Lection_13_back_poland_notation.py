# ==================================================
#
#   Lection 13.
#
#   asymptotics: O(N)
#
# ==================================================

from module import A_stack
import ast

def isint(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def backPolandNotation(notation:list):
     for token in notation:
          if isint(token):
               A_stack.push(token)
          else:
               y = A_stack.pop()
               x = A_stack.pop()
               z = eval(str(x) + str(token) + str(y))
               A_stack.push(z)
               
     return A_stack.pop()

notation = ['2', '7', "+", 5, "*"]

print(backPolandNotation(notation))

