class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        
        for i in range(2, n+1):
            if self.isPrime(i):
                dp[i] = i
            else:
                for j in range(i//2, 0, -1):
                    if i % j == 0:
                        dp[i] = min(dp[i], dp[j] + i//j)
                        break
        
        return dp[n]
    
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True