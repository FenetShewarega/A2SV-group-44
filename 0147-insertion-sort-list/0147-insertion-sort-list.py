# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        
        node = head.next
        head.next = None
        
        while node:
            next_node = node.next
            
            prior = dummy
            
            
            while prior.next and prior.next.val > node.val:
                prior = prior.next
                
                
            node.next = prior.next
            prior.next = node
            
            node = next_node
        
        node = dummy.next  
        head = None 
        while node:
            
            next_node = node.next
            
            node.next = head
            head = node
            
            node = next_node
            
        return head