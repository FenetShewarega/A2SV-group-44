# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_level = -1
        sum_values = 0

        def dfs(node, level):
            nonlocal deepest_level, sum_values

            if not node:
                return

            if level > deepest_level:
                deepest_level = level
                sum_values = node.val
            elif level == deepest_level:
                sum_values += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return sum_values