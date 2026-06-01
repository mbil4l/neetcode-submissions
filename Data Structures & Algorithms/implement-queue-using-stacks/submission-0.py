class MyQueue:

    def __init__(self):
        self.pushstk = []
        self.popstk = []

    def push(self, x: int) -> None:
        self.pushstk.append(x)

    def transfer(self):
        for num in self.pushstk[::-1]:
            self.popstk.append(self.pushstk.pop())

    def pop(self) -> int:
        if not self.popstk: self.transfer()
        return self.popstk.pop()


    def peek(self) -> int:
        if not self.popstk: self.transfer()
        return self.popstk[-1]
        

    def empty(self) -> bool:
        if not self.pushstk and not self.popstk: return True
        else: return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()