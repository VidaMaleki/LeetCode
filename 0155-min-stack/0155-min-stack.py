class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float("inf")

    def push(self, val: int) -> None:
        self.min_num = min(self.min_num, val)
        self.stack.append((val, self.min_num ))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_num = self.stack[-1][1]
        else:
            self.min_num = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()