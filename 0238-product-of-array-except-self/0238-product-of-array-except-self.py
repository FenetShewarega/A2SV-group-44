class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,2,3,4]
        1 ,1,2,6 
        # 24 12 
        
               
        lis=[]
        lis2=[]
        mul=1
        mul2=1

        for i in range (len(nums)):
            if i < 1:
                lis.append(1)
            else:   
                mul*=(nums[i-1])
                lis.append(mul)
        # print(lis)    
        for i in range((len(nums)-1),-1,-1):
            if i > len(nums) - 2  :
                lis[i]*=1
            else:
                mul2*=(nums[i+1])
                lis[i] *= mul2

        return lis
        
        
         
        
                
            
            
            
            
            
            
            
            