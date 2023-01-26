class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for j in range(len(nums)):
            for i in range(len(nums) - 1):

                comp_1 = ""
                comp_2 = ""
                comp_1 += str(nums[i])
                comp_1 += str(nums[i+1])
                comp_2 += str(nums[i+1])
                comp_2 += str(nums[i])
                
                if  int(comp_1) < int(comp_2) :
                    nums[i] , nums[i+1] = nums[i+1] , nums[i]
                    
                    
        nums =list((map(str,nums)))
        
        return str((int("".join(nums))))             
                    



        