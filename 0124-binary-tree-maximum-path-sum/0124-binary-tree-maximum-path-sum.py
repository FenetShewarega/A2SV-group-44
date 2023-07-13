class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_path_sum(node):
            if not node:
                return 0
            left_sum = max(0, max_path_sum(node.left))
            right_sum = max(0, max_path_sum(node.right))
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            return max(left_sum, right_sum) + node.val
        
        max_path_sum(root)
        
        return self.max_sum