class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0] * n
        maxOr = 0
        for x in nums:
            maxOr |= x
        return self.f(0, nums, n, 0, maxOr)

    def f(self, i: int, nums: List[int], n: int, c: int, maxOr: int) -> int:
        if i == n:
            if c == maxOr:
                return 1
            else:
                return 0
        pick = self.f(i + 1, nums, n, c | nums[i], maxOr)
        notpick = self.f(i + 1, nums, n, c, maxOr)
        return pick + notpick