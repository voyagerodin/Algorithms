
def generate_seq(N, prefix=[]):
    if len(prefix) == N:
        print(*prefix)
        return
    for x in range(1, N + 1):
        if x not in prefix:
            generate_seq(N, prefix + [x])
generate_seq(4)
