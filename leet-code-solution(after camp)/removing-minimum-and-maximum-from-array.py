class Solution(object):
    def minimumDeletions(self, nums):
        
        num = sorted(nums)
        maxx= num[-1]
        minn = num[0]
        count_1 = 1
        count_2 = 1 
        v1 = 0 
        v2 = 0
        for i in range(len(nums)):
      
             
            if  nums[i] == maxx:
                v1 = count_1
                count_2+=1
            elif nums[i] == minn:
                v2 = count_2
                count_1+=1
                
            else:
                
                count_1 += 1
                count_2 += 1
        return min(min(max(v1,v2) , len(nums) + 1 - max(v1,v2) + min(v1,v2)),(len(nums) - min(v1,v2) + 1))
    
            
      