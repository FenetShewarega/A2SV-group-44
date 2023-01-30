class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        left = 0
        right = len(skill) -  1
        count = 0 
        tot = 0
        target = skill[left] + skill[right] 
        while left < right : 
            if skill[left] + skill[right] == target :
                count +=  1
                tot += skill[left] * skill[right]
            right -= 1
            left += 1
       
        # if count == (len(skill) / 2):
        return tot if count == (len(skill) / 2) else -1
            
        