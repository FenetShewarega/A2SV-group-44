class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def diagonalgiven(m, n):
            diag = []
            while m < len(mat[0]) and n >= 0:
                diag .append(mat[n][m])
                n-=1
                m+=1
            return diag    
            
        out_put=[]
        di = []
        for row in range(len(mat)):
            
            diagonal = diagonalgiven(0,row)
            di.append(diagonal)
          
        for col in range(1,len(mat[0])):
            
            diagonal_ = diagonalgiven(col,len(mat)-1)
            di.append(diagonal_)
            
        for i in range(len(di)):
            if i%2 == 1:
                di[i].reverse()
            out_put.extend(di[i])
    
        return out_put        