class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        self.dire_arr =[[0,1],[1,0] ,[-1,0],[0,-1]]
        x = 0
        vis = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    vis.add((i,j))
                    tup = (i , j)
                    self.dfs(vis ,tup,matrix)
                    x = max(len(vis) , x)
                    vis=set()
        return x             
    def dfs(self , vis , tup,matrix):
    
        for matrix[tup[0]][tup[1]] in matrix:
            for i in self.dire_arr:
                new_x = tup[0] + i[0]
                new_y = tup[1] + i[1]
                if new_x < len(matrix) and new_x >= 0 and new_y < len(matrix[0]) and new_y >= 0:
                    if matrix[new_x][new_y] == 1:
                        vis.add((new_x , new_y))
                        new_tup = (new_x , new_y)
                        self.dfs(vis , new_tup,matrix)
                        
                
                
        
        
        