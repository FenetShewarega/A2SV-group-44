class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        
        dp= [[0 for i in range(n)] for j in range(n)] 
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
            else:
                dp[i][i+1] =max( dp[i ][j] , dp[i+1][i+1])
        for leng in range(3, n + 1):
            for i in range(n - leng + 1):
                j = i + leng - 1

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

                
        x = 0            
        for i in range(n):
            x = max(x,max(dp[i]))
        # print(dp)   
        return x        
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        