class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        r=len(nums)-1
        lis=[]
        l=0
        while  l < len(nums):
            if nums[l] + nums[r] == k:
                return ([l+1,r+1])
            else:   
                
                if nums[l] + nums[r] >k:
                    r-=1
                else :
                    l+=1
        
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
      
        