class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        x = max(nums)
        for i in range(n ):
            while nums[i] != i + 1:
                
                if nums[i] < n  and nums[i] > 0 and nums[i] != nums[nums[i] - 1] :
                    nums[nums[i] -1 ] ,nums[i] = nums[i] , nums[nums[i] -1]
                else:
                    break
        
        for i in range(n):
            if i != nums[i] - 1:
                return i + 1
        return max(nums) + 1
        

                   
       
                
                         
                
                 