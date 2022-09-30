# Algorithm for Detector Generator
import math

def Dis(ab, Ag):
    result = list()
    for i, j in zip(ab, Ag):
        result.append(math.sqrt((ab[i] - Ag[j]) ** 2))
    res = sum(result)
    if res == 0:
        print("Self")
    else:
        print("Stored In Database as Antibody")
