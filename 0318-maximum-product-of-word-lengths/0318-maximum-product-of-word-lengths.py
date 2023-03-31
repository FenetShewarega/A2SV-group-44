class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        a = ord("a")
        wrd = [0 for i in range(len(words))]
        
        for i in range(len(words)) :
            for alph in words[i]:
                x = ord(alph)
                wrd[i] = wrd[i] | 1 << x - a
                
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if wrd[i] & wrd[j] == 0:
                    res = max(res , (len(words[i] ) * len(words[j]) ))
        return res
                    
                