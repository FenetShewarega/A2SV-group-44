# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        s= set()
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False     
            
        