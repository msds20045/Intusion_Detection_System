# Compute Total of the squares of all observations
def SS(X,T):
  result = list()
  for i, j in zip(X, T):
    result.append(i * (j*j))
  return result

# Compute Correction Factor
def CF(T):
  result = list()
  for i in zip(T):
    result.append((i * i )/ len(T))
  return result

