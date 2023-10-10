# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        dic = defaultdict(int)
      
        sol = [] 
       
      
        def traverse( root):
            if not root :
                return '#'

            r = str(root.val) + traverse(root.right) + traverse(root.left)

            dic[r]+=1
            if dic[r] == 2:
                sol.append(root)

            return r
        traverse(root)
        return sol
    
     