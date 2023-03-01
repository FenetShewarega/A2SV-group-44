class Solution:
    
    def scoreOfParentheses(self, s: str) -> int:
        stack =[]
        score_stk = []
        score = 0
        spec = 1
        
        for i in range(len(s)):
            if s[i] == "(" and s[i+1] == ")":
                score += spec
            if s[i] == "(":
                
                spec *=  2
            if s[i]  == ")":
                # s.pop(-1)
                spec //= 2
        return(score)        
                
                
                                
                                 

        