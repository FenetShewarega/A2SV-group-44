class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []            
        for i in spells:
            if (i * potions[0]) >= success:
                ans.append(len(potions))
            else:
                if (i * potions[-1]) < success:
                    ans.append(0)
                else:
                    j = 0
                    left = 0
                    right = len(potions) - 1
                    while left <= right :
                        mid = (left + right ) // 2
                        if (i * potions[mid]) >=  success:
                            j = mid
                            right = mid - 1
                        else:
                            left = mid + 1
                    ans.append(len(potions) - j)
        return ans   


   
               