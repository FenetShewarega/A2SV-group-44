class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        store = {n : 1}
  
        def dp(i):
          
            if i in store:
                return store[i]
            if s[i] == "0":
                return 0
            res = dp(i + 1)
            if (i + 1 < n ) and  (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456" )):
                res += dp(i + 2)
            store[i] = res
            return res
                                                                              
                                                                              
        
        return dp(0)