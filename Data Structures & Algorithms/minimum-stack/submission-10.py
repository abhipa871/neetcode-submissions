class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = float('inf')
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.min:
            self.min = val
            self.min_stack.append(self.min)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min_stack.pop()
            self.min = self.min_stack[-1] if len(self.min_stack) else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
