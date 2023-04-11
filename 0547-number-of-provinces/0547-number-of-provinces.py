class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        visited  = set()
        count = 0 
        self.dic = defaultdict(list)
        for i in range(len(c)):
            for j in range(len(c)):
                 if c[i][j] == 1 :
                    self.dic[i ] .append(j)
        for i in range(len(c)):
            if i not in visited:
                count+=1
                self.dfs(i , visited) 
        return count
    def dfs(self , n, visited):
        
        visited.add(n)
        for nei in self.dic[n]:
            if nei not in visited:
                    self.dfs(nei , visited)
            




