class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dic = defaultdict( int )
        counter=[]  
        
        for i in cpdomains:
            
            elm = list(i.split())
            elmm = (elm[1].split("."))
            i=0
         
            while i < len(elmm):
                dic[".".join(elmm[i:])] += int(elm[0])
                i += 1 
                
        concat = [str(val) + " " + key for key,val in dic.items()]
        
        return concat