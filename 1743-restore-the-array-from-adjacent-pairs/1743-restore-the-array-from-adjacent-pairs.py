class Solution:
    def restoreArray(self, adjacentPairs):
        adj = defaultdict(list)
        vis = set()
        arr = []
        start = None

        for pair in adjacentPairs:
            num1, num2 = pair
            adj[num1].append(num2)
            adj[num2].append(num1)
        
        for num, adj_nums in adj.items():
            if len(adj_nums) == 1:
                start = num
                break
        
        self.dfs(start, adj, vis, arr)
        return arr
    
    def dfs(self, start, adj, vis, arr):
        vis.add(start)
        arr.append(start)
        for num in adj[start]:
            if num not in vis:
                self.dfs(num, adj, vis, arr)