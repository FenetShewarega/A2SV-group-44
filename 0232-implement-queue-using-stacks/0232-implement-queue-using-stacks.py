class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)
    def pop(self) -> int:
        
        if len(self.s2) == 0:
            for i in range(len(self.s1)):
                val = self.s1.pop()
                self.s2.append(val)
        return self.s2.pop()        
        
        
          # return self.s1.pop()
        
    def peek(self) -> int:
        if len(self.s2) == 0:
            return (self.s1[0])
        else:
            return( self.s2[-1])
        
            
        
    def empty(self) -> bool:
        
        
           return (True if len(self.s1) == 0 and len(self.s2) == 0 else False)
             
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# [3]
# [1 2   [1,2]

# for i in range(len(s1)):
#     s2.append(s1.pop())
# s1.append(x)
# for j in range(len(s)):
#     s1.append(s2.pop)
    
    