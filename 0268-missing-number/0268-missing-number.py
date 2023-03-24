class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)):
            if nums[i] == len(nums):
                temp = nums[i]
                nums[i] = nums[-1]
                nums[-1] = temp
        
            while nums[i]< len(nums) and nums[i] != i:
                nums[nums[i]] , nums[i] = nums[i] , nums[nums[i] ]
                
                
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            