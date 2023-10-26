# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.tot = 0
        
        def traverse(root):
            
            if not root:
                return 
            
            traverse(root.right)
            self.tot += root.val
            root.val = self.tot
            traverse(root.left)
        traverse(root)
        return  root
      
            
            