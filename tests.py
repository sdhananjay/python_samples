
t1 = [3, 6, 7, 5, 3, 5, 6, 2, 9, 1]
t2 = [2, 7, 0, 9, 3, 6, 0, 6, 2, 6]
#t1.sort()
#t2.sort()

count=0
for i in t1[:]:
    current = t2[0]
    for j in t2[:]:
        if i > j:
           continue
        if i < j:
           if current > j:
              current = j
           continue
    print(i)
    print(current)
    print("------------------------")
    if current > i:
        count += 1
    t1.remove(i)
    t2.remove(current)
print(count)
print("------------------------")

