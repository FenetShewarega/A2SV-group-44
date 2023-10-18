# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

            
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        sol = []
        
        def dfs(node, tot, path):
            if not node:
                return
          
            tot += node.val
        
            
            if not node.left and not node.right:
                if tot == targetSum:
                    path.append(node.val)
                    sol.append(path) 
                return
            
            dfs(node.left, tot, path +[node.val])  
            dfs(node.right, tot, path +[node.val])  
            
           
     
        
        dfs(root, 0, [])
        return sol