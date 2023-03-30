class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        count  = 0 
        for j in range(63):
            if 1 << (j) & x != 1 << (j) & y :

                count += 1
            
            
        return count
            