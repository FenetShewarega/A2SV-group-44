class Solution:
    def findSmallestSetOfVertices(self, n: int, e: List[List[int]]) -> List[int]:
    
        ans = set()
        sol =[ ]
        i = 0
        while i < len(e) :
            ans.add(e[i][1])
            i+=1
        print(ans)    
        for i in range(n):
            if  i not in ans:
                sol.append(i)
        return sol
         
 