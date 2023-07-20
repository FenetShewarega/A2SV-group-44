class Solution:
    def findRedundantConnection(self, edge: List[List[int]]) -> List[int]:
        n = len(edge)
        adj = [[] for _ in range(n+1)]
        vis = [False] * (n+1)
        for i in edge:
            vis = [False] * (n+1)
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            if self.dfs(i[0], -1, adj, vis):
                return i
        return []
    def dfs(self, node: int, parent: int, adj: List[List[int]], vis: List[bool]) -> bool:
        vis[node] = True
        for it in adj[node]:
            if not vis[it]:
                if self.dfs(it, node, adj, vis):
                    return True
            elif it != parent:
                return True
        return False
    
  