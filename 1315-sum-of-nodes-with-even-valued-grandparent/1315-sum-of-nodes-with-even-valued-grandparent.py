# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        def dfs( node, par_node , grad_node):
            
            if not node :
                return 0
            
            tot = 0
            if grad_node.val % 2 == 0:
                tot += node.val
            
            return tot + dfs(node.left,node ,par_node) + dfs(node.right , node,par_node)
            
        return dfs(root, TreeNode(-1), TreeNode(-1))
            
            
       
     
#         self.tot = 0
#         self.travers(root)
#         return self.tot
#     def travers(self,root):
#         if not root:
#             return
      
        
#         if root.val % 2 == 0:
            
#             if root.left and root.left.right :
#                 self.tot+= root.left.right.val
#             if root.left and root.left.left:
#                 self.tot += root.left.left.val
#             if root.right and root.right.right :
#                 self.tot+= root.right.right.val
#             if root.right and root.right.left:
#                 self.tot+= root.right.left.val
#         self.travers(root.left)
#         self.travers(root.right)
            
            
        
        
        
        
# #         self.path = []
# #         self.paths = []
        
# #         self.travers(root,path)
# #         for i in paths:
# #             for j in range(len(i)):
                
                
        
# #     def travers(self, root , path):
# #         if not root:
# #             return []
# #         path.append(root.val)
# #         if not root.left and not root.right:
# #             self.paths.append(path)
            
# #         else:
# #             if root.left:
# #                 self.travers(root.left ,path)
# #             if root.right:
# #                 self.travers(root.right ,path)
           
# #         return  (self.paths)