class Solution:
    def totalFruit(self, f: List[int]) -> int:
        left=0
        right=0
        dic=defaultdict(int)
        mx=0
       
        while right < len(f):
            if len(dic) < 2 or f[right] in dic :
                dic[f[right]] +=1
                right+=1
                mx=max(mx,right-left)
            else:
                dic[f[left]] -= 1
                if dic[f[left]] == 0:
                    del dic[f[left]]
                left +=1
        return mx        