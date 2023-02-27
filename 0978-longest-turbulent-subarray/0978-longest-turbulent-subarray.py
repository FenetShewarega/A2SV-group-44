class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize = 1
        left = 0
        right = 0
        while  right < (len(arr)) - 1:
                
                if arr[right - 1] > arr[right] < arr[right + 1] or arr[right - 1] < arr[right] > arr[right + 1] :                                                    
                    right += 1
                    maxSize = max(maxSize , right - left+1)  
                else:
                    right+=1                                                                 
                    left = right-1
        
        if len(arr) >  1 and arr[-1] != arr[-2]:
            maxSize = max(2 ,maxSize)
            
        
        return maxSize           

           