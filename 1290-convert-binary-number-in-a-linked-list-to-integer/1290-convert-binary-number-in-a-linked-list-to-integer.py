# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        curr = head
        sol = ''
        while curr:
            sol+= str(curr.val)
            curr=curr.next
            
        number = int(sol, 2)
        return(number)