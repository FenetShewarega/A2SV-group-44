class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
           
        hold = defaultdict(int)
        holder = []
        counter = [0 for i in range(len(nums)+1)]
        for req in requests:
            counter[req[0]] += 1
            counter[req[1] + 1] -= 1
                
        tot = 0
        for i in range ( 1 , len(counter)):
            counter[i]+= counter[i -1 ]
        counter.pop() 
        counter.sort(reverse = True)
        nums.sort(reverse = True)
        ans=0
        for i in range(len(counter)):
            ans+=(counter[i]*nums[i])
        
        return ans%(10**9+7)
       
       
 