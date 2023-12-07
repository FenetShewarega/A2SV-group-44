class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        dic ={}
        # k=10
        left= 0
        right =10
        while right <= len(s):
            dic[s[left:right]] =dic.get(s[left:right] , 0) + 1
            right+=1
            left+=1 
        ans =[]   
        for key in dic.keys():
            if dic[key] > 1:
                ans.append(key)
        return ans
    
    
        