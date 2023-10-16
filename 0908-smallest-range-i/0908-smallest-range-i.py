class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        if nums[-1]- nums[0] <= 2*k:
            return 0
        else:
            return (nums[-1] - nums[0] - (2*k) )