class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        def bounded(p , q):
            if q >= len(text1) or p >= len(text2) or p < 0  or q < 0:
                return False
            else:
                return True 
            
    
        n = len(text1)
        m = len(text2)
        
        dp = [[  0 for i in range(n)] for j in range(m)]
     
        for i in range(m):
            for j in range(n):
                
               
                if text1[j] == text2[i]:
                   
                    if bounded(i - 1 , j - 1 ):
                      
                    
                        dp[i][j] += (dp[i - 1 ][j-1] + 1)
                        print
                    else:
                        dp[i][j] += 1
                        
                else:
                   
                    
                    if bounded(i -1 , j - 1) :
                        dp[i][j] = max(dp[ i -1][j] , dp[i][j-1])
                    elif bounded(i-1 , j):
                          
                        dp[i][j] = (dp[i -1][j])
                    elif bounded( i ,j -1):
                        # print(i , j)
                        dp[i][j] = dp[i][j-1]
                    
                
        x = 0            
        for i in range(m):
            x = max(x,max(dp[i]))
        # print(dp)   
        return x        
                    
        
        
        