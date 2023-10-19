# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        new_node = TreeNode() 
        
        
        def travers(root1 , root2):
            
            if root1 == root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            op1 = self.travers(root1.left, root2.left)
            op2 =  self.travers(root1.right, root2.right)
            op3 =  self.travers(root1.left, root2.right)
            op4 =  self.travers(root1.right, root2.left)
            return (op1 and op2  or op3 and op4)

        return travers(root1 , root2)
                
            
                
                
                
                
                
              
            
            
            

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
class Solution:
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))