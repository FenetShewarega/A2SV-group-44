class Solution:
    def mySqrt(self, x: int) -> int:
        
        right = x
        left = 0
        while left <= right:
            mid = (right + left) // 2
            
            if  mid ** 2 < x :
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
               
               return mid    
        return right  
                
        