class Solution:
    def dfs(self, node: int, parent: int, adj: List[List[int]], hasApple: List[bool]) -> int:
        totalTime, childTime = 0, 0
        for child in adj[node]:
            if child == parent:
                continue
            childTime = self.dfs(child, node, adj, hasApple)
            if childTime or hasApple[child]:
                totalTime += childTime + 2
        return totalTime
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return self.dfs(0, -1, adj, hasApple)