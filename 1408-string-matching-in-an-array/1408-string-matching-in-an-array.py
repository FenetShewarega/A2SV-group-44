class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        new_list = []
        for i in range(len(words)):
            
            for j in range(len(words)):
                if j != i :
                    if words[i] in words[j] and words[i] not in new_list:

                        new_list.append(words[i])
        return new_list 
        