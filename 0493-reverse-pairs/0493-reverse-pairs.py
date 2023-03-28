class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.merge(nums,0,len(nums)-1)
        return self.count
    def merge(self,nums,left,right):
        if left == right:
            return [nums[left]]
        mid = (left + right) // 2
        
        left_nums = self.merge(nums,left, mid )
        right_nums = self.merge(nums,mid+1, right)
        
        
        return self.checker(left_nums , right_nums)
        
    def checker(self,arr1,arr2):
        for j in range(len(arr2)):
            self.count += len(arr1) - bisect.bisect(arr1,2 * arr2[j])
            
        left = 0
        right =0 
        res = []
        while left < len(arr1) and right < len(arr2):
            
            if arr1[left] < arr2[right]:
                
                res.append(arr1[left])
                left+=1
                
            else:
                res.append(arr2[right])
                right+=1
        res.extend(arr1[left:] or arr2[right:])
        
        return res

                
    
    
    
        