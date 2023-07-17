class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.dic = defaultdict(list)
        for i in range(len(edges)):
            self.dic[edges[i][0]].append(edges[i][1])
            self.dic[edges[i][1]].append(edges[i][0])

        if n == 1:
            return True

        visited = set()
        self.dfs(source, visited)
        return destination in visited

    def dfs(self, n, visited):
        visited.add(n)
        if n in self.dic:
            for nei in self.dic[n]:
                if nei not in visited:
                    self.dfs(nei, visited)