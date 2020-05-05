from itertools import permutations
from copy import deepcopy

if __name__ == "__main__":

    L1="3 6 7 5 3 5 6 2 9 1"
    L2="2 7 0 9 3 6 0 6 2 6"

    #L1 = "20 30 50"
    #L2 = "60 25 40"

    GR = [int(x) for x in L1.split()]
    BB = [int(x) for x in L2.split()]


    GR.sort(reverse=True)
    BB.sort()
    L1 = deepcopy(GR)
    L2 = deepcopy(BB)
    l1 = []
    l2 = []

    print(GR)
    print(BB)

    combinations = []
    count = 0

    while BB:
        i = 0
        length = len(BB)
        print(length)
        for j in range(length):
            print("--------------")
            print(GR[i], BB[j])
            print("--------------")
            if GR[i] > BB[j]:
                print("greater condition")
                print("{} is greater than {}".format(GR[i], BB[j]))
                if j >= (length - 1):
                    print("{} is last element in BB {}".format(j, BB[j]))
                    print("should be winning condition")
                    print(GR[i], BB[j])
                    combinations.append((i, j))
                    l1.append(GR[i])
                    l2.append(BB[j])
                    GR.pop(i)
                    BB.pop(j)
                    print(l1)
                    print(l2)
                    break
                continue
                print("serch for next combination")
            else:
                print("Non-greater condition")
                print("{} is not greater than {}".format(GR[i], BB[j]))
                '''
                if length == 1:
                    print("{} is last element in BB {}".format(j, BB[j]))
                    print(GR[i], BB[j])
                    combinations.append((i, j))
                    l1.append(GR[i])
                    l2.append(BB[j])
                    print(l1)
                    print(l2)
                    GR.pop(i)
                    BB.pop(j)
                    break
                else:
                '''
                print("{} is not last element in BB {}".format(j, BB[j]))
                print(GR[i], BB[j])
                combinations.append((i, j-1))
                l1.append(GR[i])
                l2.append(BB[j-1])
                print(l1)
                print(l2)
                GR.pop(i)
                BB.pop(j-1)
                break
    print(l1)
    print(l2)

