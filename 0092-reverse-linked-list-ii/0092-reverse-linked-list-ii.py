# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = None
       
        index = 0
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr   and index <= right:
            
            if index == left -1:
                first = curr
            if index == left :
                start = curr
            while curr and index >= left and index <= right:
                    print(curr)
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    index += 1
                    
            if index >= right :
            
                break
            
            curr = curr.next       
            index += 1
            
        first.next = prev
        start.next = curr
        
        return dummy.next
                
            
        