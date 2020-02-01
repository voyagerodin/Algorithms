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
               assert brace in ")]", "Все верно! Как и ожидалось - пришла закрывающаяся скобка: " + str(brace)

               if A_stack.is_empty():
                    return False
               left = A_stack.pop()

               if left == "(":
                    right = ")"
               elif left == "[":
                    right = "]"
               
               if right != brace:
                    return False
          isStackEmpty = A_stack.is_empty()
     return isStackEmpty

S1 = "asdfasdf(llkjlkj[dddddf]sdfsdf(sdfsf)]fsdf)])"
S2 = "[]([])"

print(isBracesSequenceCorrect(S2))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)