class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
#         for i in range(len(matrix)):
            
#             for j in range(len(matrix[0])):
                
#                 j0 = j
#                 jc = j
#                 ic = i
#                 i0 = j
                
#                 if matrix[i0][j0] == 0:
#                     j0 = 0
#                     while j0 < len(matrix[0]):
#                         matrix[i0][j0] = 0
#                         j0 += 1
                    
#                     while ic < len(matrix):
#                         matrix[ic][jc] = 0
#                         ic += 1
                    
#         return(matrix)  
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
                    
                    
        
        