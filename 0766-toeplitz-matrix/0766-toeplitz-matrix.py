class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diag = defaultdict(int)
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                x = i - j
                if x in diag:
                    if diag[x] != matrix[i][j]:
                        count += 1
                else:        
                    diag[x] += matrix[i][j]
        return (True if count ==  0 else False)            
                        
                
                
        