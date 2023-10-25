class Solution:
   
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        def rotateMatrix(matrix):
            rotated = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    rotated[j][n - i - 1] = matrix[i][j]
            
            return rotated

        for _ in range(4):
            if mat == target:
                return True
            mat = rotateMatrix(mat)

        return False