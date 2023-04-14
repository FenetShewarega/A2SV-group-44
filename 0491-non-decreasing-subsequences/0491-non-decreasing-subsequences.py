class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol = set()
        res = []
        def helper(st):
        
         

            if st == n  :
                if len(res) >= 2 :
                    sol.add(tuple(res))
                return
            
            if not res or res[-1] <= nums[st]:
                
                
                res.append(nums[st])
                helper( st + 1  )
                res.pop()
            
            helper( st + 1  )
        helper(0 )
        return sol 