""""          Fast exponentiation  """""


def expon(a: float, n: int):
    if n == 0:
        return 1
    else:
        return expon(a, n - 1) * a

print(expon(3, 5))

def exponBin(a, n):
    if n==0:
        return 1
    elif n%2 == 1:
        return exponBin(a, n-1) * a
    else:
        return exponBin(a**2, n//2) * a

print(exponBin(2, 8))