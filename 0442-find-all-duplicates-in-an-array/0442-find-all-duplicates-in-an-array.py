class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        
        duplicate = set()
        for i in range(len(nums)):
            while nums[i] - 1 != i:
                
                if nums[i] ==  nums[nums[i] - 1]:
                    
                    duplicate.add(nums[i])
                    break
                else:
                    nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]  
        return list(duplicate)
       