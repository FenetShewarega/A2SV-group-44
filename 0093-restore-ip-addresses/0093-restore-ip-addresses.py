from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, parts, current):
            
            if parts == 4 and start == len(s):
                result.append(".".join(current))
                return
            
            if parts == 4 or start == len(s):
                return
            
            for length in range(1, min(4, len(s) - start + 1)):
          
                if s[start] == '0' and length > 1:
                    return
                segment = s[start:start+length]
                if int(segment) > 255:
                    return
                
                current.append(segment)
                backtrack(start + length, parts + 1, current)
                current.pop()
        
        result = []
        backtrack(0, 0, [])
        return result