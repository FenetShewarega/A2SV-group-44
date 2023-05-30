class Solution:
    def tribonacci(self, n: int) -> int:
        
        self.store = defaultdict(int)
        val = self.dp(n)
        return val
    def dp(self,n):
        if n == 1 or n == 2:
            return 1
        if n == 0:
            return 0
        if n not in self.store:
            self.store[n] = self.dp(n-3) + self.dp(n-1) + self.dp(n-2)
        return self.store[n]
        
    