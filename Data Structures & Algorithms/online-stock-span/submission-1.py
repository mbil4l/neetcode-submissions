class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        
        self.stack.append(price)
        
        if len(self.stack) == 1: return 1
        else:

            res, i = 0, 0

            while i < len(self.stack) and price >= self.stack[-1 - i]:
                res += 1
                i += 1
            
            return res
            



        


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)