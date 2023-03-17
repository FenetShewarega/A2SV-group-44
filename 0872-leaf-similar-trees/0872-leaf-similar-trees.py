# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result1 = self.traverseRoot1(root1 , [])
        result2 = self.traverseRoot1(root2, [])
        if result1 == result2:
            return True
        else:
            return False
        
        
    def traverseRoot1(self,root ,path1):
        
        
        if not root :
            return []
        if  not root.left and not root.right:
            path1.append(root.val)
        else:
            self.traverseRoot1(root.left , path1)
            self.traverseRoot1(root.right , path1)
        return path1
 
        
        