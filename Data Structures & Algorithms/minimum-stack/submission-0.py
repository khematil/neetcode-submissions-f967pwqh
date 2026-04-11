class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        return

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minStack:
            return -1
        else:
            return self.minStack[-1]
        
