# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def travers(node):
            if not node:
                return 
            if node == p or node == q:
                return node
            
            left  = travers(node.left)
            right = travers(node.right)
            if left and right :
                return node
            
            return left or right 
            
        return travers(root)
     