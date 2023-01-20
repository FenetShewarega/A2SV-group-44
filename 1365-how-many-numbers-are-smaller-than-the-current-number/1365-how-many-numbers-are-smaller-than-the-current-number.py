class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out=[]
        count=0
        for i in nums:
            for j in range (len(nums)):
                if i > nums[j-1]:
                    count=count+1
            out.append(count) 
            count=0
        return (out)
