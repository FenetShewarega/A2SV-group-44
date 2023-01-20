class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        x = len(word1)
        y = len(word2)
        maxi = max(x , y)
        new_list = []
        for i in range(maxi):
            
            while len(word1) < maxi : 
                word1.append(" ")
            while len(word2) < maxi :
                word2.append(" ")
                
        for i in range(maxi):
            if word1[i] != " ":
                new_list.append(word1[i])
                
            if word2[i] != " "    :
                new_list.append(word2[i])
                
                
                
        return("".join(new_list))
     