class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, res = prices[0], 0

        for r in prices:

            l = min(l, r)
            res = max(r - l, res)
        
        return res

            