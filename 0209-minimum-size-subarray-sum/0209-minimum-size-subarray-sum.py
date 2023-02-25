class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right = 0
        mn = len(nums)+1
        total =0 
        for right in range(len(nums)):
            total+=nums[right]
            while total >= target:
                total-=nums[left]
                mn= min(mn, right-left+1)
                left+=1
        return mn if mn != len(nums) + 1 else 0         
        