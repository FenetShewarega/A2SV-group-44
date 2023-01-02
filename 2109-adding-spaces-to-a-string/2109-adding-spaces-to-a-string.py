class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
       
        j=0
        lis = []
        for i in spaces:
            lis.append(s[j:i])
            j = i                
        lis.append(s[j:])
        
        return(" ".join(lis))         
            
