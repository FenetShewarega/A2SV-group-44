class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped = [[0 for i in range(c)] for i in range(r)]
        m =len(mat)
        n = len(mat[0])
        
        out,inn =[],[]        
        cnt = 0
        # row,col=len(mat),len(mat[0])
        if m*n != r*c:
            return mat
        for i in range(m):
            for j in range(len(mat[i])):
                out.append(mat[i][j])
        for i in range(r):
            inn+=[out[cnt:cnt+c]]
            cnt = cnt + c

        return inn
                
                
        
        