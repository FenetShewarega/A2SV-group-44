class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s2 =list(map(str , s2))
        s1 = list(map(str , s1))
        n = len(s2)
        
        count_s1 = defaultdict(int)
        S = len(s1)
        if n < S:
            return 
        for i in s1:
            count_s1[i] += 1
        count_s2 = defaultdict(int) 
        
        
        
        for right in range(S) :
            count_s2 [s2[right]] += 1
            if count_s2 == count_s1:
                return True
            
        left = 0     
        for right in range(S, n):
            
            count_s2[s2[right]] += 1
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del  count_s2[s2[left]]
            left+=1    
            if count_s2 ==  count_s1:
                return True
        return False    
                
            
            