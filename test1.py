''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def total_win_fights(t1, t2):
    count = 0
    for i in t1[:]:
        current = t2[0]
        for j in t2[:]:
            if i > j:
                continue
            if i < j:
                if current > j:
                    current = j
                continue

        if current > i:
            count += 1
        t1.remove(i)
        t2.remove(current)

    return count

def find_max_fights_wins(total_fights, members, team1, team2):
    return total_win_fights(team1, team2)

if __name__ == '__main__':
    N = int(input())
    members = int(input())
    Gpowers = [int(x) for x in input().split()]
    Bpowers = [int(x) for x in input().split()]

    max_wins = find_max_fights_wins(N, members, Gpowers, Bpowers)
    print(max_wins)


