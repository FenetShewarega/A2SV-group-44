from collections import defaultdict 
n = int(input())
matrix = [] 
dic = defaultdict(list)
for i in range(n):
    row = list(map(int , input().split()))
    matrix .append(row)

for i in range(n):
    for j in range(n):
        
        if matrix[i][j] == 1:
         
            dic[i+1].append( j + 1)

r = []  
for i in dic:
    for j in dic[i]:
        x = [i , j]
        x.sort()
        if x not in r:
            r.append(x)

print(len(r))
