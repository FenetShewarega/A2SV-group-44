# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
            fast = head
            slow = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            temp = None

            while slow:
                temp_ = slow.next
                slow.next = temp
                temp = slow
                slow = temp_

            while temp:
                if temp.val != head.val:
                    return False
                temp = temp.next
                head = head.next

            return True
