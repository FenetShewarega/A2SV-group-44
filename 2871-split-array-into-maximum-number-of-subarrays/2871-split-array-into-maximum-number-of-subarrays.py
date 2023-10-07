class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
       

        n = len(nums)
        count = 0
        left = 0
      
        tot  = nums[0]
        while left < n:
            tot &= nums[left]
            if tot == 0:
                count += 1
                if left != n -1:
                    tot = nums[left + 1]
            left += 1
        if count == 0:
            count =1
        return count
            
            
            
                
                
                
                
                
     