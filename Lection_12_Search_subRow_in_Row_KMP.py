# ==================================================
#
#   Lection 12.
#   Поиск значений префикс-функции для строки.
#
#   asymptotics: O(N)
#
# ==================================================

def searchPrefix(S):
    pi = [0] * len(S)
    for i in range(1, len(S)):
        p = pi[i-1]

        while S[i] != S[p] and p > 0: 
            p = pi[p-1]
        if S[i] == S[p]:
            p += 1

        pi[i] = p
    return pi

def searchInString(sub:str, S:str):
    income = []
    div = '#'
    stringConcat = sub + div + S

    prefixList = searchPrefix(stringConcat)

    for i in range(0, len(prefixList)):
        if len(sub) == prefixList[i]:
            income.append(i - len(sub) - len(div) - 1)
    
    return income

sub = "guru"
string = "kjhgurulkjlkjgurugurugurulkjlkjggguruuuuulkjlkjgur"
sub1 = "jjjj"
string1 = "nnjjjjnnnjjjj"

print(searchInString(sub1, string1))