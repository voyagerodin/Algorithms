# ==================================================
#
#   Lection 12.
#
#   asymptotics: O(N)
#
# ==================================================
""" 
  """

def prefixFunction(S):
    pi = [0] * len(S)

    for i in range(1, len(S)):
        p = pi[i-1]

        while p > 0 and S[i] != S[p]: 
            p = pi[p]

        if S[i] == S[p]:
            p += 1
        pi[i] = p
    return pi 

S = "abcabcab"
# S = "aabaabaaaabaabаaab"
# S = "abacabacda"
print(prefixFunction(S))