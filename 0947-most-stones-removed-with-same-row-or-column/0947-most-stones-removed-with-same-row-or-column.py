class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        vis = [False] * n
        c = 0
        for i in range(n):
            if vis[i]:
                continue
            self.dfs(stones, i, vis)
            c += 1
        return n - c
    def isvalid(self, pos1: List[int], pos2: List[int]) -> bool:
        if pos1[0] == pos2[0]:
            return True
        if pos1[1] == pos2[1]:
            return True
        return False
    
    def dfs(self, stones: List[List[int]], idx: int, vis: List[bool]) -> None:
        vis[idx] = True
        n = len(stones)
        for i in range(n):
            if vis[i]:
                continue
            if self.isvalid(stones[i], stones[idx]):
                self.dfs(stones, i, vis)
    
 