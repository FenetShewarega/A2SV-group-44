class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        self.vis = []
      
        self.colors = [0 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            if self.dfs(i,graph):
                continue
        self.vis.sort()
        return self.vis

    def dfs(self,node,graph):

        if self.colors[node] == 1:
            return True
        if self.colors[node] == 2:
            return False
        self.colors[node] = 1
        for neigh in graph[node]:
            if self.dfs(neigh,graph):
                return True
        self.colors[node] = 2
        self.vis.append(node)
        return False




        