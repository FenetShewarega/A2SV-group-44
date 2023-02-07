class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

 
        r=len(matrix)              
        c=len(matrix[0])
        matrix_ = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(matrix[i][j])
            matrix_.append(temp)    
      
              
        for i in range(r): 
            for j in range(c):
                if matrix[i][j] == 0:

                    left = 0 
                    right = 0
                    while left < c :
                        matrix_[i][left] = 0
                        left += 1
                    while right < r :   
                        matrix_[right][j] = 0
                        right += 1

        for i in range(r):
            for j in range(c):
                matrix[i][j] = matrix_[i][j]
        
                    
                    
        
        