class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        sol=[]
        self.vis= set()
        self.graph = defaultdict(list)
        for i , j in ((richer)):
            self.graph[j].append(i)
        print(self.graph)
        for x in range(len(quiet)):
            self.vis = set( )
            res = self.dfs(x,quiet)
            res = sorted(res)
            res= list(res)
            if res:
                sol.append(res[0][1])
            else:
                sol.append(x)
        return(sol)
            
    def dfs(self , node,quiet):
        # print(self.graph)
        if node in self.graph:
            self.vis.add((quiet[node] , node))
            for neig in self.graph[node]:
                if (quiet[neig],neig )not in self.vis:
                    self.vis.add((quiet[neig] , neig))
                    self.dfs(neig,quiet)
        return self.vis