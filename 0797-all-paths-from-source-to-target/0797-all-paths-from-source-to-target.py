class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.res=[]
        self.n=len(graph)-1
        return self.dfs(0,[0],graph)
    def dfs(self,i,path,graph):
        if i==self.n:
            self.res.append(path)
        else:
            for j in graph[i]:
                if j not in path :
                    self.dfs(j,path+[j],graph)
   
        return self.res
