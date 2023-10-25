"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        


        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_nodes = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(level_nodes)

        return result