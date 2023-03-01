class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.helper(rowIndex)
       
    def helper(self, rowIndex: int):
        
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        
        take = self.helper(rowIndex - 1)
        take = [0] + take + [0]
        ans = [1 for i in range(rowIndex + 1)]
        for i in range(1,rowIndex):
            ans[i] = take[i] + take[i + 1]
        return (ans)