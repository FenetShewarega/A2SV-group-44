class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0
        ret = -inf
        for num in nums:
            total = max(total+num , num)
            ret = max(ret, total)
        return ret
           
                
                
                
            
       
                
            
        
        
        
        
        