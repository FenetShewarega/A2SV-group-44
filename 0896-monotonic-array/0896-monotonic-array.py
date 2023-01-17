class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec = 0 
        incr = 0
        for i in range(len(nums)-1):
            j = i+1
            if nums[i] <= nums[j]:
                dec += 1
            if nums[i] >= nums[j]:
                incr += 1
        return True if incr == len(nums) -1 or dec == len(nums) -1 else False       
        