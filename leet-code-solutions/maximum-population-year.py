class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_range = 0
        min_range = 2051
        for i in logs:
            max_range = max(i[1] ,max_range)
            min_range = min(i[0] , min_range)
        max_range = max_range -  1949
        min_range = min_range  - 1949
        
        p_s = [0 for _ in range(max_range + 1)]
        
        for i in logs:
            
            p_s[i[0] - 1949] += 1
            p_s[i[1] - 1949] -= 1
        for i in range( 1, len(p_s)):
            p_s[i] = p_s[i - 1] + p_s[i]
        max_val = max(p_s)
        for i in range(len(p_s)):
            if p_s[i] == max_val:
                return i + 1949
        