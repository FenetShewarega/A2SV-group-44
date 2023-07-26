class Solution:
  
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res = [1]
                    self.dfs(grid1, grid2, i, j, res)
                    ans += res[0]
        return ans
    def dfs(self, grid1: List[List[int]], grid2: List[List[int]], x: int, y: int, res: List[int]) -> None:
        m, n = len(grid1), len(grid1[0])
        if x < 0 or y < 0 or x >= m or y >= n:
            return
        if grid1[x][y] == 0 and grid2[x][y] == 1:
            res[0] = 0
        if grid2[x][y] == 0:
            return
        grid2[x][y] = 0
        self.dfs(grid1, grid2, x + 1, y, res)
        self.dfs(grid1, grid2, x, y + 1, res)
        self.dfs(grid1, grid2, x - 1, y, res)
        self.dfs(grid1, grid2, x, y - 1, res)