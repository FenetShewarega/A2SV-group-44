# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:\
        
        fast  = head 
        slow  = head
        count = 0
        while fast and fast.next:
            if count == 0 :
                slow = slow.next
                fast = fast.next.next
            else:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
            if slow == fast:
                fast = head
                count+=1
     
            if count == 2:
                return slow
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        