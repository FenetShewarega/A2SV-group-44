class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            count  = 0 
            for j in range(63):
                if 1 << (j) & i  :
        
                    count += 1
            ans.append(count)
            
        return(ans)
            
            