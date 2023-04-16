# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        root = head
        val = []

        while root:
            val.append(root.val)
            root = root.next
        
        # val.sort()
        i = 0
        j = len(val) - 1
        max_val = 0
        while(i < j):
            max_val = max(max_val, val[i] + val[j])
            i = i + 1
            j = j - 1
        
        return max_val
        