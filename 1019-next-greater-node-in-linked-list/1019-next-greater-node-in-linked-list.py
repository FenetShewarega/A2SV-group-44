# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stk=[]
        slow = head
        
        while head :
            stk.append(head.val)
            head = head.next
         
        sol  = [0 for i in range(len(stk))]
        stack=[]
        for i in range(len(stk)):
            
            while stack and stk[stack[-1]] <  stk[i]:
                sol[stack.pop()] = stk[i]
            stack.append(i)
            
  
            
        return sol