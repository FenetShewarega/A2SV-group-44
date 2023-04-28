class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        queue = deque([(root, TreeNode(-1), TreeNode(-1))])
        while queue:
            curr_node, par_node, grand_node = queue.popleft()
            # print(curr_node.val, par_node.val, grand_node.val)
            
            if grand_node.val % 2 == 0:
                ans += curr_node.val
            if curr_node.left:
                queue.append((curr_node.left, curr_node, par_node))
                
            if curr_node.right:
                queue.append((curr_node.right, curr_node, par_node))
        
        return ans
        
