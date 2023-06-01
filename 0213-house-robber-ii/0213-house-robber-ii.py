class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        @cache
        def dp( i ,fromlast):
            if i >= n:
                fromlast = False
                return 0 
            if n == 2:
                return max(nums)
            if fromlast:
                return (max( nums[i] + (dp( i - 2 , fromlast) if  i - 2 > 0 else 0), dp(i - 1 , fromlast) if i -1 > 0 else 0))
            else:
           
                return max( nums[i] + (dp( i - 2,fromlast) if  i - 2 >= 0 else 0),dp(i - 1,fromlast ) if i -1 >= 0 else 0)
        return max(dp( n -1 ,True) ,dp(n-2 , False))