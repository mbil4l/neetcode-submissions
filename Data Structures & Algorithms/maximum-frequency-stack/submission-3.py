class FreqStack:

    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int)
        self.idx = 0
        

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush_max(self.heap, (self.cnt[val], self.idx, val))
        self.idx += 1
        

    def pop(self) -> int:
        _, _, res = heapq.heappop_max(self.heap)
        self.cnt[res] -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()