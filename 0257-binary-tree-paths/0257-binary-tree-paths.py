# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  

    def binaryTreePaths(self,root):
        paths = []
        if root:
            self.dfs(root, "", paths)
        return paths

    def dfs(self,node, path, paths):
        path += str(node.val)
        if not node.left and not node.right:
            paths.append(path)
        else:
            path += "->"
            if node.left:
                self.dfs(node.left, path, paths)
            if node.right:
                self.dfs(node.right, path, paths)