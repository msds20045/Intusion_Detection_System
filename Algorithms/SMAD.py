# Compute Total of the squares of all observations
def SS(X, T):
    result = list()
    for i, j in zip(X, T):
        result.append(i * (j * j))
    res = sum(result)
    return res


# Compute Correction Factor
def CF(T):
    result = list()
    for i in T:
        result.append((i * i) / len(T))
    return sum(result)


# Compute Total Sum of Squares
def TotalSS(X, T):
    ss = sum(SS(X, T))
    cf = CF(T)
    result = ss - cf
    return result


# Compute Sum of Squares Total
def SST(T, H):
    cf = CF(T)
    result = list()
    for i in T:
        result.append((i * i) / H - cf)
    return sum(result)


def SSB(T, X, K):
    cf = CF(T)
    result = list()
    for i, j in zip(X, T):
        result.append((i * (j * j)) / K - cf)
    res = sum(result)
    return res


A = [1, 2, 3]
B = [1, 2, 3]

print(SSB(A, B, 1))
ss = SS(A, B)

cf = CF(A)
