class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid) 
        maxlocal = [[0 for i in range(n - 2)] for i in  range(n-2)]
        max_= 0 
      
        for i in range(len(maxlocal)):
            for j in range(len(maxlocal)):
                u = max(grid[i][j] , grid[i][j+1] , grid[i][j+2] )
                m = max(grid[i+1][j],  grid[i+1][j+1] , grid[i+1][j+2] )
                l = max(grid[i+2][j],  grid[i+2][j+1] , grid[i+2][j+2] )
                val = max(u,m,l)
              
                maxlocal[i][j] = val
        return maxlocal
            
            
            
                                                                                                                            