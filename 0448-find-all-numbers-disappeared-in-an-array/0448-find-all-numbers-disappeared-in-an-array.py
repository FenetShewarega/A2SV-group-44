class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:\
        
        l = []
        ans =[]
        for i in range(len(nums)):
            while nums[i] - 1 != i:
                if nums[i] ==  nums[nums[i] - 1]:
                    break
                else:
                    nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]  

        for i in range(1 ,len(nums) + 1):
            l.append(i)
        for i in range(len(nums)):
            if l[i] != nums[i]:
                ans.append(l[i])
        return ans
            
        