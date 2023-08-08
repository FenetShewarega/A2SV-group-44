class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) % 3 != 0:
            while len(nums) % 3 != 0:
                nums.append(0)
        
        for i in range(0, len(nums) - 2, 3):

            if nums[i] != nums[i + 2]:
                return nums[i]
        
 