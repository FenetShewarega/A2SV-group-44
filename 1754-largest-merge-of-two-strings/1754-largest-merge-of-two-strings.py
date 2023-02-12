class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        merge =[]
        word1 = list(word1)
        word2 = list(word2)
        
        while len(word1) != 0 and len(word2) != 0 :
            if word1 > word2:
                merge .append( word1[0] )
                word1.pop(0)
            else:
                merge.append(word2[0])
                word2.pop(0)
        merge += word1
        merge += word2
        return "".join(merge)       