class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c = 0
        left = 0 
        right = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        while left <= right:
            
            mid = ( right + left )//2
            if nums[mid] < target : 
                left = mid + 1
            
            else:
                if nums[mid] == target:
                    c += 1
                right = mid - 1
                
        return left  if c > 0 else -1
        