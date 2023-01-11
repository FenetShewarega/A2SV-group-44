class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        out_put = []
        s = s.split(" ")
        m=0
        
        for i in s:
            if len(i) > m:
                m = len(i)
            
        for i in range(len(s)):
            while len(s[i]) < m:
                s[i]+=" "
            
        for i in range(m):
            st = ""
            for j in range(len(s)):
                st += s[j][i]
                
            st = list(st)
            while st[len(st) - 1] == ' ':
                (st).pop()
               
            out_put.append("".join(st) )
            
        return(out_put)        
            
        
        
        
        

        
        