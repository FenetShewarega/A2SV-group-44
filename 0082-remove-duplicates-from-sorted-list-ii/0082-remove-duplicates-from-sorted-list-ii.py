# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        dummy = ListNode()
        dummy.next = head
        cur = head
        prev = head
        temp = dummy
        
        while cur:
            count = 0
            cur_val = cur.val

            while cur and prev.val == cur.val:                
                cur = cur.next 
                count += 1
                
            if count > 1:
                temp.next = cur
                prev = cur
            
            else:
                temp = temp.next
                prev = cur
                
        return dummy.next
            
        
        
        