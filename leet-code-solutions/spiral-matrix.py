class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
    
        res = []
        row, col = 0, 0
        left, right, bottom, top = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        x = 0

        while left <= right and top <= bottom:
            
            if x == 0:
                
                for i in range(left, right + 1):
                    
                    res.append(matrix[top][i])
                x = 1
                
                top += 1
                
            elif x == 1:
                
                for i in range(top, bottom + 1):
                               
                    res.append(matrix[i][right])
                               
                x = 2
                right -= 1
                
            elif x ==2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                x = 3
                bottom -= 1
            elif x ==  3:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                x = 0
                left += 1
        return res

        