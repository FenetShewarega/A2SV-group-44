class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        @cache
        def dp(i , curr_sum):
                
            if i >= n:
                return 0
            if curr_sum == amount:
                return 1
            if curr_sum > amount :
                curr_sum = 0
                return 0
            return dp(i + 1 , curr_sum ) + dp(i , curr_sum + coins[i])
        return dp(0,0)