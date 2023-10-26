# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.sol = 0
        flag = True
        def traverse(root , flag):
            if not root:
                return 
            if not root.left and not root.right and flag :
                self.sol += root.val
            left = traverse(root.left,True) 
        
            right = traverse(root.right,False)
        traverse(root,False)
        return(self.sol)
        