class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count=0
        dic={0:1}
        _sum = 0
        for i in nums:
            _sum+=i
            if _sum % k in dic:
                
                count +=  dic[_sum % k]
            dic[_sum % k] = dic.get(_sum % k , 0 ) + 1    
        return count      
         
        [4,5,0,-2,-3,1]
        
5