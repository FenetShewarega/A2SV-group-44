n = int(input())
matrix = [] 
for i in range(n):
    row = list(map(int , input().split()))
    matrix .append(row)
for i in range(n):
    adj = []

    for j in range(n):
        if matrix[i][j] == 1:
            adj.append(j+1)
    print(len(adj),*adj)
