class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0] * (len(s) + 1)
        
        for _from, _to, inc in shifts:
            prefix[_from] += 1 if inc else -1
            prefix[_to + 1]  -=  1 if inc else -1
                   
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        ans = []
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            
            idx = (idx + prefix[i]) % 26
            
            idx += ord('a')
            
            ans.append(chr(idx))
        return ''.join(ans)
            
            
        