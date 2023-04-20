n = int(input())
matrix = [] 
sink = []
source = []
for i in range(n):
    row = list(map(int , input().split()))
    matrix .append(row)
for i in range(n):
    count = 0
    c = 0
    for j in range(n):
        if matrix[j][i] == 1:
            count += 1
    for z in range(n):

        if matrix[i][z] == 1:
            c +=1
    
    if c > 0 and count == 0:
            source.append(i+1)
    if c == 0 and count > 0:
        sink.append(i+1)
    if c == 0 and count == 0:
        sink.append(i+1)
        source.append(i+1)   
source.sort()
sink.sort()
print(len(source) , *source)
print(len(sink), *sink)
