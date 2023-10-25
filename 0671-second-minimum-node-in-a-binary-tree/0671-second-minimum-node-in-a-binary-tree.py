# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if not root:
                return []
            left = traverse(root.left)
            right = traverse(root.right)
            
            return left + [root.val] + right
        sol = traverse(root)
      
        sol = set(sol)
        sol = list(sol)
        sol.sort()
       
    
        print(sol)
        return sol[1] if len(sol) >= 2 else -1
        
            