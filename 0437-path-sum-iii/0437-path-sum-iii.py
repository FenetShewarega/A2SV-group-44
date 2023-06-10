# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.helper(root, sum, [])
        return self.count
        
    def helper(self, node, target, path):
        if not node:
            return
        path.append(node.val)
        curr_sum = 0
        for i in range(len(path)-1, -1, -1):
            curr_sum += path[i]
            if curr_sum == target:
                self.count += 1
        self.helper(node.left, target, path)
        self.helper(node.right, target, path)
        path.pop()
        
       
        
        