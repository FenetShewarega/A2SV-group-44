class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def dp(i , j):
            if i >= n:
                return 0
            return  triangle[i][j] + min(dp( i + 1 , j + 1 if j < len(triangle[i]) else 0) ,
                       dp( i + 1,  j if j < len(triangle[j]) else 0))
        return dp(0,0)