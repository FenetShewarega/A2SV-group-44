# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def rob_helper(node):
            if not node:
                return (0, 0)

            left = rob_helper(node.left)
            right = rob_helper(node.right)

            rob_node = node.val + left[1] + right[1]
            not_rob_node = max(left) + max(right)

            return (rob_node, not_rob_node)

        return max(rob_helper(root))