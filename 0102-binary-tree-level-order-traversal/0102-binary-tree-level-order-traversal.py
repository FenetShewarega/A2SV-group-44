# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self. ans = []
        sol = []
        self.dfs(root,0)
    
        for i in range(len(self.ans)):
            dic[self.ans[i][1]].append(self.ans[i][0])
        for i in dic:
            sol.append(dic[i])
        return sol
    
    def dfs(self,root ,d):
        
        
        if not root:

            return 
        
        self.ans.append([root.val ,d])
        self.dfs(root.left  , d+1)
        self.dfs(root.right ,d + 1)
        return self.ans  
        
        
    
        
            
        
        
        
#         if not root:
#             return
        
#         queue = deque([root])
#         res  = []
        
#         while queue:
#             curr = []
#             allow = len(queue)
            
#             while allow > 0:
                
#                 node = queue.popleft()
#                 curr.append(node.val)
               
#                 allow -= 1
                
#                 if node.left:
#                     queue.append(node.left)
                
#                 if node.right:
#                     queue.append(node.right)
                    
#             res.append(curr)
        
#         return res
    
         # if not root: