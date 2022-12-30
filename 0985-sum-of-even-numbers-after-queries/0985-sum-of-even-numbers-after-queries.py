class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        out_put = []
        
        hasht = defaultdict(int)
        t=0
        for i in nums: 
            if i % 2 == 0 :
                t+=i
        
        for i in  range(len(nums)):
            
            if nums[queries[i][1]] % 2 == 0 :
                t -= nums[queries[i][1]]
                
            nums[queries[i][1]] = nums[queries[i][1]] + queries[i][0]
            x =  nums[queries[i][1]] 
            if x % 2 == 0 :
                t+=x
            out_put.append(t)
            
        return(out_put)