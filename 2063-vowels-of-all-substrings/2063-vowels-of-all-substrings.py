class Solution:
    def countVowels(self, word: str) -> int:
      
        s = 0
        n =len(word)
        dic = {'a':1, 'e':1,'i':1,'o':1,'u':1}
        
        for i in range(n):
                if word[i] in dic:
                    s += (n-i)*(i+1)
        return s
            
        