# ==================================================
#
#   Lection 13.
#
#   asymptotics: O(N)
#
# ==================================================

from module import A_stack

def isBracesSequenceCorrect(S:str):
     """ Проверяет корректность скобочной последовательности
     из круглых и квадратных скобок () []
     
     >>> isBracesSequenceCorrect("(([()]))[]")
     True
     >>> isBracesSequenceCorrect("[]")
     True
     >>> isBracesSequenceCorrect("()")
     True
     >>> isBracesSequenceCorrect("[()]()[[[(())]]][]")
     True
     >>> isBracesSequenceCorrect("([)]")
     False
     >>> isBracesSequenceCorrect("(")
     False
     >>> isBracesSequenceCorrect(")")
     False
     >>> isBracesSequenceCorrect("[")
     False
     >>> isBracesSequenceCorrect("]")
     False
          """

     for brace in S:
          if brace not in "()[]":
               continue

          if brace in "([":
               A_stack.push(brace)
          else:
               assert brace in ")]", "Катастрофа!!! ожидалась закрывающаяся скобка: " + str(brace)

               if A_stack.is_empty():
                    return False
               left = A_stack.pop()
               assert left in "([", "Ожидалась открывающая скобка: " + str(brace)
               if left == "(":
                    right = ")"
               elif left == "[":
                    right = "]"
               if right != brace:
                    return False
     
     return A_stack.is_empty()

S = "("

print(isBracesSequenceCorrect(S))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)