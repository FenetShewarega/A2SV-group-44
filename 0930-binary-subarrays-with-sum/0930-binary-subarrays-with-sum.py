class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic={0:1}
        count=0
        total=0
        for i in nums:
            total+=i
            if total - goal in  dic:
                count += dic[total - goal]
            dic[total] = dic.get((total) ,0)+1
        return count    
        