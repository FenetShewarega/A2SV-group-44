class Solution:
    def partitionString(self, s: str) -> int:
        
        
        g = []
        count = 0
        for right in range(len(s)):
            if s[right] in g: 
                count+=1
                g=[]
               
            
            g.append(s[right])      
            if right == len(s) - 1 and  g:
                count += 1
                
        return count