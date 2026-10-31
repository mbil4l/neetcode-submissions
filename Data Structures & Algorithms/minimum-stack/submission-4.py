# class MinStack:

#     def __init__(self):
#         self.stack = []
        

#     def push(self, val: int) -> None:
#         if not self.stack: self.stack.append((val, val))
#         else: self.stack.append((val, min(self.stack[-1][1], val)))
        
#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1][0]

#     def getMin(self) -> int:
#         return self.stack[-1][1]
        
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, value: int) -> None:
        self.stack.append((value, min(self.min, value)))
        self.min = self.stack[-1][1]
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack: self.min = self.stack[-1][1]
        else: self.min = float("inf")
        

    def top(self) -> int:
        if self.stack: return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack: return self.stack[-1][1]
