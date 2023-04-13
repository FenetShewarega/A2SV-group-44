# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.string = ""
     
        res = self.travers(root)
        return res
    
    def travers(self ,root):
      
        if root:
            self.string += str(root.val)
            if root.left or root.right:
                    self.string += '('
                    self.travers(root.left)
                    self.string+=')'
      
    
     
            if root.right:
                self.string+="("
                right = self.travers(root.right) 
                self.string += ")"        

        return  self.string        