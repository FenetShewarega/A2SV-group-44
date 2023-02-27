class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for i in range(n)]
        
        for rec in queries:
            matrix[rec[0]][rec[1]] += 1
            if rec[2] + 1 < n :
                matrix[rec[2]+ 1][rec [1]] -= 1
                if rec[3] + 1 < n:
                    matrix[rec[2] + 1][rec[3] + 1] += 1
            if rec[3] + 1 < n :
                matrix[rec[0] ][rec[3] + 1] -= 1
        prefx  = [[0 for i in range(n)] for i in range(n)] 
        total = 0
        for i in range(n):
            for j in range(n):
                   
                if i == 0:
                    total+= matrix[i][j]
                    prefx[i][j] = total
                elif j == 0  and i != 0:
                    prefx[i][j] = matrix[i][j] + prefx[i-1][j]
                else:    
                        prefx[i][j]= matrix[i][j] + prefx[i-1][j] + prefx[i][j-1] - prefx[i-1][j-1]
                
                
    
        return(prefx)      