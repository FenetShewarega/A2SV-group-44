class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid) 
        maxlocal = [[0 for i in range(n - 2)] for i in  range(n-2)]
        max_= 0 
        directions = [(0, 0), (0, 1), (0, 2), 
                      (1, 0), (1, 1), (1, 2), 
                      (2, 0), (2, 1), (2, 2)]
        
        for i in range(len(maxlocal)):
            for j in range(len(maxlocal)):
                val = -inf
                for dx, dy in directions:
                    val = max(val, grid[i + dx][j + dy])
                maxlocal[i][j] = val
        return maxlocal
            
            
            
                                                                                                                            