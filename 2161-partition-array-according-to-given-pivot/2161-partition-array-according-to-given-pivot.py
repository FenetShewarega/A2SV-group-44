class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        new_nums = []
        for i in range(len(nums)):
            
            if nums[i] < pivot  :
                new_nums.append(nums[i])
                
        i = 0 
        for i in range(len(nums)):
            
            if nums[i] == pivot:
                new_nums.append(nums[i])
                
        i =0         
        for i in range(len(nums)):
            
            if nums[i] > pivot:
                new_nums.append(nums[i])
                
        return new_nums
        