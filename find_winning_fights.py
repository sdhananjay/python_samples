from itertools import permutations
from copy import deepcopy

def find_max_winning_fights(GR, BB):
    l1 = []
    l2 = []
    count = 0

    while BB:
        i = 0
        length = len(BB)
        for j in range(length):
            if GR[i] > BB[j]:
                if j >= (length - 1):
                    l1.append(GR[i])
                    l2.append(BB[j])
                    GR.pop(i)
                    BB.pop(j)
                    break
                continue
            else:
                l1.append(GR[i])
                l2.append(BB[j-1])
                GR.pop(i)
                BB.pop(j-1)
                break
    
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            count += 1
    print(count)

if __name__ == "__main__":

    L1="3 6 7 5 3 5 6 2 9 1"
    L2="2 7 0 9 3 6 0 6 2 6"

    #L1 = "20 30 50"
    #L2 = "60 25 40"

    GR = [int(x) for x in L1.split()]
    BB = [int(x) for x in L2.split()]


    GR.sort(reverse=True)
    BB.sort()
    find_max_winning_fights(GR, BB)
