class ListNode:
    def __init__(self, val=0, next=None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.page = ListNode(homepage)
        
    def visit(self, url: str) -> None:

        URL  = ListNode(url, prev=self.page)
        self.page.next = URL
        self.page = self.page.next

    def back(self, steps: int) -> str:
        
        
        count = 0
        while self.page.prev and count < steps:
            self.page = self.page.prev
            count += 1 
        return self.page.val
      
       
    def forward(self, steps: int) -> str:
        
        count = 0 
        while self.page.next and count < steps:
            self.page = self.page.next
            count += 1 
        return self.page.val
        
        
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)