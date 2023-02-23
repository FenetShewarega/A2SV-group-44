class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0
        tot = 0
        prefix =[]
        mn = -inf
        maxf  = 0
        count = 0
        right = 0
        mn_tot = -inf
        for right in range(len(nums)):
            if nums[right] < 0:
                count+=1
            total += nums[right]
            if total <= 0:
                # left = right + 1
                mn_tot = total
                total = 0
            mn = max(mn_tot , mn) 
            maxf = max(maxf, total)
        return maxf  if count != len(nums) else mn
            
          
                
                
                
            
       
                
            
        
        
        
        
        