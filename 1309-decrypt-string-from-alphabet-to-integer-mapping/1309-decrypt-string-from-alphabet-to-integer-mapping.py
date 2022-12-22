class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        res=''
        right=2
        left=0
        n=len(s)    
        
        while  left < n:
            if right < n and s[right] == "#":
                res+= chr(int(s[left:right]) + 96) 
                right+=3
                left+=3
                
            else:
                res+=chr(int(s[left])+96)
                left+=1
                right+=1
                
        return res     
        
        
       
        