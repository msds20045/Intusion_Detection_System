# Compute Total of the squares of all observations
def SS(X,T):
  result = list()
  sum=0
  for i, j in zip(X, T):
    result.append(i * (j*j))
  return result

# Compute Correction Factor
def CF(T):
  result = list()
  s = len(T)
  for i in zip(T):
    result.append((i * i )/ s)
  return result

# Compute Total Sum of Squares
def TotalSS(X,T):
  ss=sum(X)
  cf=sum(T)
  result=ss-cf
  return result

A=[1,2,3]
B=[1,2,3]
ss=SS(A,B)

cf=CF(A)
B=TotalSS(ss,A)
print(B)