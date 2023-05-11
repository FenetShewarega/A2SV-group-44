class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        sol = [[] for i in range(n)]
        self.vis = set()
        self.store = defaultdict(list)
        for i , j in (edges):
            self.store[j].append(i)
        for i in range(n):
            # if i not in self.vis:
            self.vis=set()
            x = self.dfs(i)
            x = list(x)
            x.sort()
            sol[i]= (x)
        return (sol)
    def dfs(self,n):
        
#         if node in self.store:
#             for neig in self.store[node]:
                
#                 self.vis.add(neig)
#                 self.dfs(neig)
#         self.vis.add(node)
        # print((self.dic))
        if n in self.store:
            for nei in self.store[n]:
                if nei not in self.vis:
                        self.vis.add(nei)
                        self.dfs(nei)

       
                
        return self.vis
        
        