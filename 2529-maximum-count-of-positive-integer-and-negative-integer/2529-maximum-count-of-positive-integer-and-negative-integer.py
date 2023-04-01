class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) -1
      
      
        while left <= right:
            
            mid =  ( left + right ) // 2
            if nums[mid] <= 0 :
                left = mid + 1
            else:
                right = mid - 1
                
                
            
        count_pos =  len(nums) - left
            
        left = 0
        right = len(nums) -1
      
      
        while left <= right:
            
            mid =  ( left + right ) // 2
            if nums[mid] >= 0 :
                right =  mid - 1
            else:
                left = mid + 1
                
                
            
        count_neg = left 
        return max(count_neg , count_pos)