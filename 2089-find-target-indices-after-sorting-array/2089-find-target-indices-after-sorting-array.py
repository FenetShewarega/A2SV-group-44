class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        k=[]
        nums.sort()
        for i in range(len(nums)):
            if target==nums[i]:
                k.append(i)
            else:
                    pass
        return k
        