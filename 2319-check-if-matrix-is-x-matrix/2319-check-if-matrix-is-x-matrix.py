class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if i == j or i == n - j - 1:
                    # Check diagonals
                    if grid[i][j] == 0:
                        return False
                else:
                    # Check non-diagonal elements
                    if grid[i][j] != 0:
                        return False

        return True