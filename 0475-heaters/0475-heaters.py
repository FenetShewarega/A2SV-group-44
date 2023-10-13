class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_rad = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            if i == 0:
                max_rad = max(max_rad, heaters[0] - house)
            elif i == len(heaters):
                max_rad = max(max_rad, house - heaters[-1])
            else:
                max_rad = max(max_rad, min(heaters[i] - house, house - heaters[i - 1]))
        
        return max_rad
               
