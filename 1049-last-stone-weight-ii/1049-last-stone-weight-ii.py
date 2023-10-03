class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
 
        total_sum = sum(stones)
        max_sum = ceil(total_sum / 2)
        dp = {} 
        def dfs(i ,tot):
            if tot >= max_sum or i == len(stones):
                return abs(tot - (total_sum - tot))
            if (i , tot) in dp:
                return dp[(i ,tot)]
            dp[(i ,tot)] = min(dfs(i+1 , tot), dfs(i+1 , tot + stones[i]))
            return dp[(i,tot)]

        return dfs(0,0)