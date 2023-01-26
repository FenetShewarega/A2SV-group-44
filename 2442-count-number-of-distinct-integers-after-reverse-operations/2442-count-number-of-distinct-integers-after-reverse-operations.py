class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        dict_count = defaultdict(int)
        for i in range(len(nums)):
           
            x = ((str(nums[i])))
           
            nums.append(int(x[::-1]))
        for i in nums:
            dict_count[i] += 1
        return(len(dict_count.values()))    