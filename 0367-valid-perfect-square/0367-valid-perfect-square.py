class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        x = num ** 0.5
        if int(x) *  int(x) == num:
            return True
        else:
            return False
        