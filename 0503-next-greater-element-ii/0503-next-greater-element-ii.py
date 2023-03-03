class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack  = []
        res = [-1 for i in range(len(nums))]
        n = len(nums)
        for i in range(n ):
            
            while stack and nums[stack[-1]] < nums[i]:
                
                x =stack.pop()
                res[x] = nums[i]
                
            stack.append(i)
            
        for i in range(n):  
            
            if stack:
                while stack and nums[stack[-1]] < nums[i]:
                    x = stack.pop()
                    res[x] = nums[i]
          
        return res
                
            
            
            
             
        