# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path = ""
        self.paths = 0
       
        return  self.helper(root , path)
      
    def helper(self,root,path):
        if not root:
            return
        path += str(root.val)
        if not root.right and not root.left:
            path
            self.paths+=int(path,2)
           
        else:
            if root.right:
                 self.helper(root.right,path)
            if root.left:
                 self.helper(root.left,path)
        return self.paths
        
                        
        
        
        
        
     

        