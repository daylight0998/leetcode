#!/usr/bin/python3
# encoding: utf-8


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if self.min_stack == [] or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(-2)
obj.push(-3)
obj.push(0)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
