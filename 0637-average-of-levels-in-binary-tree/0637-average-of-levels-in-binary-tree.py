# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        dictionary = defaultdict(list)

        def traverse(  root ,  row  ):

            if not root:
                return 

            dictionary[row].append(root.val)

            traverse(root.left , row+1 )
            traverse(root.right ,  row+1)
           
        traverse(root , 0)
        ave = []
        for i in dictionary:
            tot = 0
            x = dictionary[i]
            size = len(x) 
            for j in range(size):
                tot += x[j]
            ave.append(tot / size)

        return ave 

        
        