class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        negative = []
        postive = []
        out_put = []
        
        for i in range(len(nums)):
            if nums[i] < 0 :
                negative.append(nums[i])
            else:
                postive.append(nums[i])
        for i in range(len(postive)):
            out_put.append(postive[i])
            out_put.append(negative[i])
        return out_put    
        