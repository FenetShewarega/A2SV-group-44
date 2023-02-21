# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
            
            index = 0
            dummy = ListNode()
            dummy.next = head
            curr = dummy
            while curr :
                index += 1
                curr = curr.next 
            l = 0
            curr = dummy
            while curr  :
                if index - n -1 == l:
                    curr.next = curr.next.next
                curr = curr.next
                l+=1
                
                
                
            return dummy.next 
            
                
                
            
            
        