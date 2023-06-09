class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        used = set()
        self.backtrack(n, used, 1)
        return self.count
    
    def backtrack(self, n: int, used: set, pos: int) -> None:
        if pos > n:
            self.count += 1
        for i in range(1, n+1):
            if i not in used and (pos % i == 0 or i % pos == 0):
                used.add(i)
                self.backtrack(n, used, pos+1)
                used.remove(i)