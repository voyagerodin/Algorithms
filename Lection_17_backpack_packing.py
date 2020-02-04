# ==================================================
#
#    Lection 17.
#    Packing backpack!
#    Укладка дискретного конечного рюкзака.
#    Каждый предмет обладает массой и стоимостью.
#    asymptotics: O(N*M)
#
# ==================================================

"""  """
def bestTotalCost(M, C, W):
     F = [[0]*(W+1) for i in range(len(M))]

     for i in range(1, len(M)):
          for w in range(1, W + 1):
               if M[i] <= w:
                    F[i][w] = max(F[i-1][w], F[i-1][w-M[i]] + C[i])
               else:
                    F[i][w] = F[i-1][w]
     return F, F[i][w]

def insideBackpack(F, M, W):
     tmp = W
     backpack = []
     for i in range(len(M)-1, 0, -1):
          if F[i][tmp] != F[i-1][tmp]:
               backpack.append(i)
               tmp -= M[i]
     return backpack

thingMass = [0, 7, 3, 1, 5, 4]
thingCost = [0, 10, 4, 2, 6, 7]
backpackMass = 12

bestCost = bestTotalCost(thingMass, thingCost, backpackMass)
print(bestCost[1])
print(insideBackpack(bestCost[0], thingMass, backpackMass))     

               
