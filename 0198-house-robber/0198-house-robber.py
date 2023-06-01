class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n= len(nums)
        @cache
        def dp( i):
            if i >= n:
                return 0
            
            return max( nums[i] + (dp( i - 2) if  i - 2 >= 0 else 0),dp(i - 1 ) if i -1 >= 0 else 0)
        return dp( n -1)
        