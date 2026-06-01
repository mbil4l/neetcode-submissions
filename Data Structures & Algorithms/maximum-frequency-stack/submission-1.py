class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int) 
        self.stacks = defaultdict(list)
        self.curmax = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        if self.cnt[val] > self.curmax: self.curmax = self.cnt[val]
        self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.curmax].pop()
        self.cnt[res] -= 1
        if len(self.stacks[self.curmax]) == 0:
            self.curmax -= 1
        return res
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()