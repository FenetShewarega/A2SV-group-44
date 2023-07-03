class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = defaultdict(int)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)
            if node == target:
                break
        
        visited = set()
        result = []
        stack = [(target, 0)]
        while stack:
            node, distance = stack.pop()
            visited.add(node)
            if distance == k:
                result.append(node.val)
            elif distance < k:
                if node.left and node.left not in visited:
                    stack.append((node.left, distance + 1))
                if node.right and node.right not in visited:
                    stack.append((node.right, distance + 1))
                if node in parent_map and parent_map[node] not in visited:
                    stack.append((parent_map[node], distance + 1))
        
        return result