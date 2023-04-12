# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        if not root:
            return True
        res = self.travers(root.left ,root.right)
        return res
        
    def travers(self , root_left , root_right):
    
        if not root_left and not  root_right:
            return True
        if ((root_left and not root_right ) or
               (root_right and not root_left)or
                    (root_right.val != root_left.val)):
            return False
            
        left = self.travers(root_left.right , root_right.left)
        right = self.travers(root_right.right ,root_left.left)
        
        return left and right and root_left.val == root_right.val
        