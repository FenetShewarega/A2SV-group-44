class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def recur(curr_amount):
            doro = inf
            if curr_amount == 0:
                return 0
            if curr_amount > 0:
               
                for c in coins:
                    doro = min(doro , recur(curr_amount - c) + 1)
            return doro 
        val =  recur(amount)          
        if val == inf:
            return -1
        else:
            return val