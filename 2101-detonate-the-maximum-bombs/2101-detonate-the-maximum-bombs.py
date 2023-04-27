class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
        self.dic = defaultdict(list)
        count = 0
        x = 0
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    if(bombs[i][0] - bombs[j][0])**2 + (bombs[i][1]-bombs[j][1] )**2 <=  bombs[i][2] ** 2 :
                           self.dic[i].append(j)
        if not self.dic:
            return 1
       
        for i in self.dic:
            if i not in visited:
                visited = set()
                self.dfs(i , visited) 
                
            x = max(len(visited ) ,x)
      
        return x
        
    def dfs(self , n, visited):
        visited.add(n)
        # print((self.dic))
        if n in self.dic:
            for nei in self.dic[n]:
                if nei not in visited:
                        self.dfs(nei , visited)

       
            