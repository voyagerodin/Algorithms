# ==================================================
#
#   Lection 10.
#   Trajectoryes number with forbidden cells.
#   asymptotics: O(N)
#
# ==================================================

def count_trajectoties(N, allowed: list):
    ''' how many trajectories exist to move from point 1 to point N
        if we move along the numeric line only to the right
        in increments of +1, +2, +3 and some cells are forbidden'''
    K = [0, 1, int(allowed[2])] + [0] * (N - 3)
    for i in range(3, N):
        if allowed[i]:
            K[i] = K[i - 1] + K[i - 2] + K[i - 3]
    return K[N-1]

allowed = [True, True, True, True, True, True, True, True, True, True]
print(count_trajectoties(10, allowed))
