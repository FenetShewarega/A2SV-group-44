class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = defaultdict(int)
        for i in nums:
            dictionary[i] += 1
        if len(dictionary) < len(nums):
            return True
        else:
            False
            
        