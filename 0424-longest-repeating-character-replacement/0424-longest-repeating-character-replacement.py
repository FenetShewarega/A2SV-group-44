class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right= 0
        left=0
        dic=defaultdict( int)
        ans = 0
        for right in range(len(s)):
            dic[s[right]]+=1
            while ((right - left +1)-(max(dic.values())) > k):
                dic[s[left]] -= 1
                left+=1
            ans = max(ans , right - left + 1)    
        return  ans     
                
                