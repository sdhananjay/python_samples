''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def find_total(N, Q, TQ):
    total = 0
    flag = True
    count = 0

    
    Q_len = len(Q)
    TQ_len = len(TQ)
    print("Q_len : {} TQ_len : {} N : {}".format(Q_len, TQ_len, N))
    if Q_len == 0 or TQ_len == 0:
        return 0
    if N != Q_len or N != TQ_len:
        return 0
    for i in range(Q_len):
        if Q[i] == 0:
            count += 1
    if count == N:
        return 0
    
    count = 0
    for i in range(TQ_len):
        if TQ[i] == 0 and Q[i] != 0:
            return 0

    while flag:
        for i in range(N):
            quantity = Q[i]
            if quantity == 0:
                flag = False
                break
            if TQ[i] <= 0:
                flag = False
                break
            balance = TQ[i] - quantity
            TQ[i] = balance
            #print("qantity : {} total_quantity : {} banlance : {}".format(quantity, TQ[i], balance))
            if balance <= 0:
                flag = False
                break
        total += 1
    return total

if __name__ == '__main__':

    #print("started")
    result = 0
    count = 0
    N = int(input())

    quantities = [int(x) for x in input().split()]
    total_quantities = [int(x) for x in input().split()]

    print(quantities)
    print(total_quantities)

    result = find_total(N, quantities, total_quantities)
    print(result)
    

        

            
        
