class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

 
        r=len(matrix)              
        c=len(matrix[0])
        row=[0]*r
        col=[0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(r):
            if row[i]==1:
                for j in range(c):
                    matrix[i][j]=0
        for i in range(c):
            if col[i]==1:
                for j in range(r):
                    matrix[j][i]=0
                    
                    
        
        