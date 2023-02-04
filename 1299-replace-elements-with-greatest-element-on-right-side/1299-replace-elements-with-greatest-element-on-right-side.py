class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        maxx = -1
        for i in range(len(arr)-1,-1,-1):
            val = arr[i]
            arr[i] = maxx
            if val > maxx:
                maxx = val
        return arr