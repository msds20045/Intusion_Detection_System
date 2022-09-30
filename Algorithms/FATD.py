# Algorithm for File Anomaly Type Detection using Positive Selection Algorithm
def Check(ab, Ag):
    for i in Ag:
        for j in ab:
            if ab[j] == Ag[i]:
                print("Self File")
                return 0
        print("Non Self File")
        print("Reading File")
