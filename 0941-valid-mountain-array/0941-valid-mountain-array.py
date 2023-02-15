class Solution(object):
    def validMountainArray(self, arr):
        
        n = len(arr)
        i = 0

        flag = False
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1

      
        if i == 0 or i == n-1:
        
            return False

  
        while i+1 < n and arr[i] > arr[i+1]:
            i += 1

      
        if i == n-1:
            flag = True 
            return(flag)
        else:
            flag  = False
            return(flag)
            
            