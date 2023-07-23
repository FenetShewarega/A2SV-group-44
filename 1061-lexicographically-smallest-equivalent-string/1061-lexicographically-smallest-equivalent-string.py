class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        representative = list(range(26))
        
        def find(x):
            if representative[x] == x:
                return x
            
            representative[x] = find(representative[x])
            return representative[x]
        
        def performUnion(x, y):
            x = find(x)
            y = find(y)
            
            if x == y:
                return
            
            if x < y:
                representative[y] = x
            else:
                representative[x] = y
        
        for i in range(26):
            representative[i] = i
            
        for i in range(len(s1)):
            performUnion(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        ans = ''
        for c in baseStr:
            ans += chr(find(ord(c) - ord('a')) + ord('a'))
        
        return ans