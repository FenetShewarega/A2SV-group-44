class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dic_arr=[(0,1),(1,0),(0,-1),(-1,0)]
        self.color = color
        self.n = len(image) 
        self.m = len(image[0])
        res = self.dfs(image,sr,sc,image[sr][sc])
        
        return res
    def dfs (self,image ,a,b , c):
        
        
        image[a][b] = self.color
        # print(image[a][b])
        # if a <  and a >= 0
        for x in range(4):
            Y = self.dic_arr[x][0]
            Z = self.dic_arr[x][1]
            
            if a + Y < self.n and a + Y >= 0 and b + Z < self.m and b + Z >= 0:
                new_x = a + Y
                new_y = b + Z
            
                if image[new_x][new_y] == c and image[new_x][new_y] != self.color:
                    
                    self.dfs(image , new_x,new_y,c)

        return image


