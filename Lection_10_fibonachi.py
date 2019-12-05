#==================================================
#
#   Lection 10.
#   Fibonachi.
#   asymptotics: O(fib(N))
#
#==================================================

def fib(n):
    ''' recursion '''
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(40))


def fibDinamic(n):
    ''' dinamic prog '''
    fibo = [0,1] + [0]*(n-1)
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

print(fibDinamic(100000))