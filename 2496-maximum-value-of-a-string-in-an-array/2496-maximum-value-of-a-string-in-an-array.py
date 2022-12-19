class Solution:
    def maximumValue(self, strs: List[str]) -> int:
     
        lis=[]
        for i in strs:
            t=0
            if i.isnumeric():
                t+=int(i)
                lis.append(t)
            else:
                t+=len(i)  
                lis.append(t)
        mx=max(lis)        
        return  mx        