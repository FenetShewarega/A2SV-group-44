from collections import defaultdict
n = int(input())
k = int(input())

l = defaultdict(list)
for i in range(k):
   
    op = list(map(int , input().split()))
    if op[0] == 1:
        l[op[1]].append(op[2])
        l[op[2]].append(op[1])
    else:
        if l[op[1]]:
            print(*l[op[1]])
