class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
#         i = 0
#         j = len(matrix[0])
#         while i < len(matrix):
#             if matrix[i][j] < target:
#                 i + = 1
#             if matrix[i][j] > 
                
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False        