class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        out_put = []
        for i in range(len(nums)):
            out_put.insert(i,nums[nums[i]])
        return(out_put)    
        