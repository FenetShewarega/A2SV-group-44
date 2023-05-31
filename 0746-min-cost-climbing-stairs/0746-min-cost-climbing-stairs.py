class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.store = defaultdict(int)
        return min(self.dp(cost , 1) , self.dp(cost , 0) )
    def dp(self,cost , i ):
        
        if i >= len(cost):
            return 0
        if i not in  self.store:
             self.store[i] = min(self.dp(cost,i+1) + cost[i], self.dp(cost , i+2) + cost[i])
        return self.store[i]
   