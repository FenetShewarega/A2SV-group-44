class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        n =len(nums)
        res = 0
        for i in range(n):
            s += nums[i]
            res = max(res,math.ceil(s/(i+1)))
        return res