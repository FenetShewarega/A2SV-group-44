# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next
class Solution(object):
    def middleNode(self, head):
        
        curr = head
        size = 0
        while curr:
            size+=1
            curr = curr.next
   
        curr = head
        for i in range(size//2):
            curr = curr.next
        return (curr)
            