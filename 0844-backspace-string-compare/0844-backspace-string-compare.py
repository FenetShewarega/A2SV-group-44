class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stk = []
        for i in s:
            if len(stack) == 0:
                if i == "#":
                    continue
                else:
                    stack.append(i)
                    
            else:    
                if i == "#":
                    stack.pop()
                else:    
                    stack.append(i)
        for i in t :
            if len(stk) == 0:
                if i == "#":
                    continue
                else:
                     stk.append(i)
            else:    
                if i == "#":
                    stk.pop()
                else:
                    stk.append(i)
        return (stk == stack)        
          