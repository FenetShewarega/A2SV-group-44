class Solution:
    def kidsWithCandies(self, c: List[int],ec: int) -> List[bool]:
        
        mx= max(c)
        # print(mx)
        res=[]
        flag= True
        for i in range(len(c)):
            
            c[i] = c[i] + ec
            
            if c[i] >= mx:
                res.append(1)
            else: 
                res.append(0)
        return res
     