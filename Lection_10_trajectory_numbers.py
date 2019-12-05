# ==================================================
#
#   Lection 10.
#   Trajectoryes number.
#   asymptotics: O(N)
#
# ==================================================

def trajectories_number(N):
    ''' how many trajectories exist to move from point 1 to point N
        if you move along the numeric line only to the right
        in increments of +1 and +2 '''
    K = [0, 1] + [0] * N
    for i in range(2, N + 1):
        K[i] = K[i - 1] + K[i - 2]
    return K[N]

print(trajectories_number(10))