class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        n = []
        for i in digits:
            num += str(i)
            
        val = (int(num) + 1)  
        
        res = list(map(int , str(val)))
       
        return res    