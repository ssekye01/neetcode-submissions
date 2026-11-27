class MinStack:

    def __init__(self):
        self.norm_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.norm_stack.append(val)
        if not self.min_stack or self.norm_stack[-1] < self.min_stack[-1]:
            self.min_stack.append(self.norm_stack[-1])
        else: 
            curr = self.min_stack[-1]
            self.min_stack.append(curr)

    def pop(self) -> None:
        if self.norm_stack:
            self.norm_stack.pop()
        if self.min_stack:
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.norm_stack:
            return self.norm_stack[-1]
        return 
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return 
        
