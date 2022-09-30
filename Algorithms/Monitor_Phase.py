# Algorithm for Monitor Phase
import math


def Dis(a, s):
    result = list()
    for i, j in zip(a, s):
        result.append(math.sqrt((a[i] - s[j]) ** 2))
    res = sum(result)
    if res == 0:
        print("Alert to machine")
    else:
        print("Accepting next feature ..")
