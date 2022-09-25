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
    ss = SS(X, T)
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


# Compute Sum of Square Error
def SSE(X, T, H, K):
    return TotalSS(X, T) - (SST(T, H) - SSB(T, X, K))


# Compute Degrees of Freedom (DF)
# DF for Total SS
def DFT(H, k):
    return H * k - 1


# DF for Sum of Squares Total
def DFt(H):
    return H - 1


# DF for Square Sum between
def DFB(K):
    return K - 1


# DF for Sum of Square Error
def DFE(H, K):
    return DFT(H, K) - (DFt(H) + DFB(K))


# Compute Mean Square (MS)
def MSA(T, H):
    return SST(T, H) / DFt(H)


def MSB(T, X, K):
    return SSB(T, X, K) / DFB(K)


def MSE(X, T, H, K):
    return SSE(X, T, H, K) / DFE(H, K)


A = [1, 2, 3]
B = [1, 2, 3]

print(SSE(A, B, 1, 1))
ss = SS(A, B)

cf = CF(A)
