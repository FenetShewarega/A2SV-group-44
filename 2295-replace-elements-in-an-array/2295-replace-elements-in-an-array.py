class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        
        repl = defaultdict(int)
        for i in range(len(nums)):
            repl[nums[i]] += i
            
        for j in range(len(op)):
            
            if op[j][0] in repl:
              
                x = repl[op[j][0]]
                nums[x] = op[j][1]
                del repl[op[j][0]]
                repl[op[j][1]] += x
                
        return nums       