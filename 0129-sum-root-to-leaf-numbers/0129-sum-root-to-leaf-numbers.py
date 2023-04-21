# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return
        self.tot = 0
        return self.dfs(root,"")
    def dfs(self,root,ans):
        
        if not root:
            return
        ans+=str(root.val)
        if not root.left and not root.right:
            self.tot += int(ans)
        else:
            if root.left:
                 left= self.dfs(root.left,ans)
            if root.right:
                right = self.dfs(root.right,ans)
        
        return self.tot 
        
        