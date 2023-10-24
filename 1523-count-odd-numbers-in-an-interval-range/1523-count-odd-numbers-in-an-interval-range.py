class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 == 0 :
            if high % 2 == 0:
                return (high - low + 1)//2
            else:
                return (high - low + 1)//2
        else:
            if high % 2 == 0:
                 return (high - low + 1)//2
            else:
                 return  ceil((high - low + 1) / 2)
                
                