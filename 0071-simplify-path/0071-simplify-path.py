class Solution:
    def simplifyPath(self, path: str) -> str:
        
            stack = []
            i = 0
            while i < len(path):
                
                cur = path[i]
                i += 1
                if cur == '/':
                    while i < len(path) and path[i] == '/':
                        cur += path[i]
                        i += 1
                        
                else:
                    while i < len(path) and path[i] != '/':
                        cur += path[i]
                        i += 1

                if cur == '..':
                    
                    if len(stack) > 0: 
                        stack.pop()
                        
                elif cur[0] != '/' and cur != '.': 
                    stack.append(cur)
                    print(stack)
        
            res = ''
            for s in stack: 
                res += ('/' + s) 

            return res if res else '/'

   