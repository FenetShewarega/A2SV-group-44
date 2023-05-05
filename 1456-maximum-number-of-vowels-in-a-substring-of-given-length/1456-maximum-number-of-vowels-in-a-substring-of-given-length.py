class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cnt = 0
        for x in range(k):
            if s[x] in vowels:
                cnt+=1
        res = cnt
        for x in range(k,len(s)):
            if s[x-k] in vowels:
                cnt-=1
            if s[x] in vowels:
                cnt+=1
            res = max(res,cnt)
        return res
                 
        