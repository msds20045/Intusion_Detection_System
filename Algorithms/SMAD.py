import math


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
    Ss = SS(X, T)
    Cf = CF(T)
    result = Ss - Cf
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


# Compute F ratio
def F1(X, T, H, K):
    return MSA(T, H) / MSE(X, T, H, K)


def F2(X, T, H, K):
    return MSB(T, X, K) / MSE(X, T, H, K)


def Critical_Diffrence(X, T, H, K, n, t):
    s = math.sqrt(MSE(X, T, H, K))
    L = len(A)
    # S=standard Error
    CD = s * math.sqrt(2 * n) * t
    absl = abs((X[0] * T[0]) - (X[L - 1]) * T[L - 1])
    if absl > CD:
        print("Usage of one feature is dependent on the usage of another feature")
    else:
        print("Usage of one feature is not dependent on the usage of another feature")


def Three_Sigma(X, T):
    result = list()
    for i, j in zip(X, T):
        result.append(i * j)
    Avg = sum(result) / len(T)
    S = sum(result) - Avg
    Square = S * S
    Avg = Avg + Square
    variance = Avg / len(T)
    One_Sigma = math.sqrt(variance)
    Two_Sigma = 2 * One_Sigma
    Three_sigma = 3 * Two_Sigma
    if X[len(X) - 1] > Three_sigma:
        print(" Capture the {TIME, SRC, SRCPORT, DST,DSTP ORT, PKTS, DATA} of the network packet")


A = [1, 2, 3]
B = [1, 2, 3]

# print(A[])
ss = SS(A, B)

cf = CF(A)
