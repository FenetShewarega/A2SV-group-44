class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        ans = []
        n = len(nums)
        
        heapify(nums)
        while i <  n:
            x = heappop(nums)
            ans.append(x)
            i+=1
        return(ans[n - k])
            
        