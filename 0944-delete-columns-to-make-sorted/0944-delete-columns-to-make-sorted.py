class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
       
        tot = 0
        for i in range(len(strs[0])):
            
            count = 0 
            for j in range(len(strs) -1 ):
                
                if  ord(strs[j][i]) <= ord(strs[j + 1][i]):
                    count += 1 
               
            if count != len(strs) - 1:
                tot += 1       
        return tot
                    
                    
                    
                    
                    
                
                
                
            
        