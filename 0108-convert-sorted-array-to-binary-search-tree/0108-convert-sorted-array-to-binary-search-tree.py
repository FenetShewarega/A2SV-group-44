# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        ln = len(nums) // 2
        root = TreeNode(nums[ln])
        root.left =  self.sortedArrayToBST(nums[:ln])
        root.right = self.sortedArrayToBST(nums[ln+1:])
        
        return root
        
        
        