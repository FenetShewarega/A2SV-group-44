# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        result = self.traverse(root)
        total = 0
        for i in range(len(result)):
            if result[i] >= low and result[i] <= high:
                total+=result[i]
        return total   
    def traverse(self,root):
    
        if not root:
            return []
        left= self.traverse(root.left)
        right = self.traverse(root.right)
        return left + [root.val ]+ right
         
        