class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      
        count = 0
        cur = 1
        i = 0

        while count < k:
            if i < len(arr) and arr[i] == cur:
                i += 1
            else:
                count += 1

            if count == k:
                return cur

            cur += 1
