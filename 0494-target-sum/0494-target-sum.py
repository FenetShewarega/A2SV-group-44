class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
         
            # self.count = 0
            self.memo = defaultdict(tuple)
          
            return  self.dp(nums,0,0,t)
            
    def dp(self,nums,i , sum,t):
        if i == len(nums):
            if sum == t:
                return 1
            else:
                return 0
        if (i,sum) in self.memo:
            return self.memo[(i,sum)]
       
        self.memo[(i,sum)] = self.dp(nums,i+1 ,sum + nums[i] , t) + self.dp(nums,i+1 ,sum - nums[i] , t)

        return self.memo[(i,sum)]
        
        