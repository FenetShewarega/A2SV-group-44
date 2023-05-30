class Solution:
    def climbStairs(self, n: int) -> int:
        self.count = 0
    
        self.store = defaultdict(int)
        val = self.dp( n ,0)
        return val
    def dp(self, n,i):
        if i == n or i == n - 1:
            return 1
        if i not in self.store:
           
            
            if i + 1 < n:
                self .store[i]  =  self.dp(n, i+2) + self.dp(n, i+1)
            else:
                self.store[i] = self.dp(n, i+1)   
        return self.store[i]    
