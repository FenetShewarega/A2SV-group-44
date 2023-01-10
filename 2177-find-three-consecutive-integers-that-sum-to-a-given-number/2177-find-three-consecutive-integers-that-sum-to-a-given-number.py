class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        out_put = [] 
        
        if num % 3 == 0:
            x = num // 3
            out_put.append(x-1)
            out_put.append(x)
            out_put.append(x+1)
        return out_put    