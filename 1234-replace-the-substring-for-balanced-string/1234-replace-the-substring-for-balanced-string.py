class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        counter = defaultdict(int)
        new =  defaultdict(int)
        for right in s:
            counter[right] += 1
            
        l = n//4    
        x=0
        for i in counter:
            if counter[i] > l:
                x += 1
                new[i] += counter[i] - l
    
        count = 0
        res = inf
        left = 0
        
        if x == 0:
            return 0
        
        for right in range(len(s)):
            
            if s[right] in new:
                new[s[right]] -= 1
                if new [s[right]] == 0: 
                    x -= 1
                    
            while x == 0 :
                res = min(res, right - left + 1)
                if s[left] in new:
                    new[s[left]] += 1
                    if new [s[left]] == 1:
                        x += 1 
                left+= 1
                
        return res
            