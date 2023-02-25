class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right =0
        total =0 
        for right in range(k):
            total+=nums[right]
            ave= total/k
        for right in range(k,len(nums))  :
            total-=nums[left]
            total+=nums[right]
            aver= total/k
            ave = max(ave ,  aver)
            left+=1
        return ave   
            
            
      