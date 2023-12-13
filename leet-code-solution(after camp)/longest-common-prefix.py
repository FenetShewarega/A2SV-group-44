class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn=min(strs,key = lambda x:len(x))
        x=len(mn)
        for i in strs:
            while i[:x] != mn[:x] :
                x-=1
        return mn[:x]
                
                  
            
                
       
                