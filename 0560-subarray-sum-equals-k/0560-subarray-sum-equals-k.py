class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        dic = defaultdict(int)
        dic[0] = 1
        total=0
        count=0
        
        for i in nums:
            total+=i
            if total - k in dic :
                count+= dic[total - k]
            dic[total] += 1
            
        return count    
    
        
        