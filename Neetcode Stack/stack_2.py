class MinStack:
    '''
    Stacks are LIFO (last in first out)
    '''
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        '''
        Push element val onto stack
        '''
        self.stack.append(val)
        
        # Append min value to min stack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        '''
        Remove element on top of the stack
        '''
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        '''
        Get top element of the stack
        '''
        return self.stack[-1]

    def getMin(self) -> int:
        '''
        Retrieve min element in the stack
        '''
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin()) # -3
print(obj.pop())
print(obj.top()) # 0
print(obj.getMin()) # -2
