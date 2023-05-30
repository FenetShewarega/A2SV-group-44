class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        self.store = defaultdict(int)
        for i in range(n+1):
            self.dp(i)
        ans = 0
    
        for i in self.store:
            ans = max(ans ,self.store[i])
        if n == 1:
            return 1
        return ans    
    def dp(self, n):
        if n == 0 :
            return 0
        if n == 1:
            return 1
        if n not in self.store:
            if n % 2 == 0:
                
                self.store[n] = self.dp(n // 2)
            else:
                self.store[n] =  self.dp(n // 2) + self.dp((n // 2) + 1)
        return self.store[n]