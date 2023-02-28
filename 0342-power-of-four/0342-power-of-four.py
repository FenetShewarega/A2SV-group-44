class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        if n == 1:
            return True
        
        elif n <= 0:
            return False
        else:
            if n % 4 == 0: 
                n = n / 4
               
            else:
                return False
        
        
    
     
        return self.isPowerOfFour(n)