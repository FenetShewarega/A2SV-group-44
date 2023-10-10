class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashValue: int) -> str:
        hash_v  = 0
        store= defaultdict(int)
        sol = []
        j = len(s) - 1
        count = -1
        while j > (len(s) - k) - 1:
            
           
            store[s[j]] += 1
         
            hash_v += (ord(s[j]) - 96) * (pow( p , (count + k),m ))
           
            count -= 1
            j -= 1
            
            hash_v %= m 
        
        if hash_v % m == hashValue:
            sol.append(s[len(s) - k :])
        left = len(s) - 1 
        right = left - k
        power = pow(p , k -1 , m) 
        while right >= 0 :
            hash_v -= ((ord(s[left]) - 96) * power )
            hash_v *= p
            hash_v += (ord(s[right]) - 96) 
            
            if hash_v % m == hashValue:
                
                sol.append(s[right :left]) 
            left -= 1
            right -= 1
            hash_v %= m
        
        return sol[-1]
            
        
           
            
            
    