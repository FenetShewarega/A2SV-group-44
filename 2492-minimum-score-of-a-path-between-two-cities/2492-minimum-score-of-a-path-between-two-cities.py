class Solution:
    def dfs(self, node, adj, visit, answer):
        visit[node] = True
        for edge in adj[node]:
            answer[0] = min(answer[0], edge[1])
            if not visit[edge[0]]:
                self.dfs(edge[0], adj, visit, answer)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))
        visit = [False] * (n + 1)
        answer = [float('inf')]
        self.dfs(1, adj, visit, answer)

        return answer[0]