class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dp =  [[-1 for _ in range(26)] for i in range(len(s))]
        
        for i in range(len(s) - 1 , -1 , -1):
            if i != len(s) - 1:
                for j in range(26):
                    dp[i][j] = dp[i + 1][j]
            x = ord(s[i]) - 97
            dp[i][x] = i
        
        sol = 0
        for word in words:
            
            count  = 0
            j = 0
            i = 0
            while j < len(word) and i < len(s):
                x = ord(word[j]) - 97
            
                if dp[i][x] != -1:
                    j += 1
                  
                    i = dp[i][x] + 1 
                    count += 1
                else:
                    break
            if count  == len(word) :
              
                sol += 1
   
        return (sol)
                    
                        
                    
                        
                        
                        
            