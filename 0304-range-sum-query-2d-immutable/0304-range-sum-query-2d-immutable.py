class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        total = 0
        self.prefx  = [[0 for i in range(len(self.matrix[0])) ] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            
            
            
            for j in range(len(self.matrix[0])):
                if i == 0:
                    total+= self.matrix[i][j]
                    self.prefx[i][j] = total
                elif j == 0  and i != 0:
                    self.prefx[i][j] = self.matrix[i][j] + self.prefx[i-1][j]
                else:    
                        self.prefx[i][j]= self.matrix[i][j] + self.prefx[i-1][j] + self.prefx[i][j-1] - self.prefx[i-1][j-1]
                    
                    
        print(self.prefx)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            row_val = 0
            
        else:
            row_val=self.prefx[row1-1][col2]
        if col1==0:
            col_val=0
        else:
            col_val=self.prefx[row2][col1-1]
        if row1==0 or col1==0:

            dig_val=  0
        else:
            dig_val = self.prefx[row1-1][col1-1]
          
        return  (self.prefx[row2][col2] - row_val - col_val  +  dig_val)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)