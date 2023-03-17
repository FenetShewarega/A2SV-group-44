# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
     
        result =  self.traverse(root , 0 ,[], targetSum)
        for i in range(len(result)):
            if result[i] == targetSum:
                return True
        return False
    def traverse(self,root , path ,paths,targetSum):
        
        if not root:
            return []
        path+=root.val
        if not root.left and not root.right:
             paths.append(path)
        else:
            if root.left:
                self.traverse(root.left ,path,paths, targetSum)
            if root.right:
                self.traverse(root.right ,path,paths, targetSum)
        return paths