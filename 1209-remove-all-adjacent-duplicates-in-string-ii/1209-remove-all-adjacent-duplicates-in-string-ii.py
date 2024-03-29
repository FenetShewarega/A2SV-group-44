class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stack = [[s[0] , 1]]
        
        for i in range( 1 , len(s) ):
            
            if stack and s[i]  == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                 stack.append([s[i] ,  1])
        # print(stack)
        val = ''
        for i in range(len(stack)):
            
            val += (stack[i][0]) * stack[i][1]
        return val
            
            
                