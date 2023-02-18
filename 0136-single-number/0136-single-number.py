class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        for i in range(len(nums)):
            
            dic[nums[i]] += 1
            
        sorted_dic = sorted( dic.items() , key = lambda x:x[1])
        
        return (sorted_dic[0][0])   
        
            
        