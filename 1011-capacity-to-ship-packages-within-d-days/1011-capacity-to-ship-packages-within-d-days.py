class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        
        l = max(w)
        r = sum(w)
        ans = []
        
        while l <= r:
            mid = (r + l)//2
            t = 1
            total = 0
            for i in range(len(w)):
                total += w[i]
                if total > mid:
                    t += 1
                    total = w[i]
            if t > days:
                l = mid + 1
            else:
                r = mid - 1
        return l