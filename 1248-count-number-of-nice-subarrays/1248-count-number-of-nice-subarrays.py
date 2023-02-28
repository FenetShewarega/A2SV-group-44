class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         d={1:3,}
#         1,1,2,1,1
        
#         1,1,0,1,1
#         1,2 2 ,3,3
#         1,2,2,3,3

        dic=defaultdict(int)
        dic[0]=1
        r=0
        count=0
        p_s=[]
        for i in nums:
            r += i % 2
            p_s.append(r)
        print(p_s)    
        for j in p_s:
            if (j - k) in dic:
                count+=dic[j-k]
            dic[j] += 1
        return count
        
