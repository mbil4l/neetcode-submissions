from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:

            m = l + (r-l)//2

            k = sum([ceil(p/m) for p in piles])
            
            if k > h:
                l = m + 1
            elif k <= h:
                res = min(res, m)                
                r = m - 1
        
        return res


        