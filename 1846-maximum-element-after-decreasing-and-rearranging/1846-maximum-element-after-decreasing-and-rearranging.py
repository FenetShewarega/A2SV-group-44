class Solution: 
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        print(set(arr))
        b = False
        for i in range(1,len(arr)):
            if abs(arr[i-1] -arr[i]) > 1:
                b = True
                if arr[i-1] < arr[i]:
                    arr[i] = arr[i-1] + 1
                else:
                    arr[i-1] = arr[i] + 1
        if b == False and len(arr) > 1:
            if max(arr) < len(arr):
                
                return max(arr)
            else:
                return len(arr)
        if max(arr) > len(arr):
            return(len(arr))
        else:
            return(max(arr))
        