from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        maxSpeed = max(piles)
        l, r = 1, maxSpeed
        res = maxSpeed

        while l <= r:

            totalTime = 0

            midSpeed = l + (r - l) // 2

            for pile in piles: totalTime += ceil(pile / midSpeed)
            
            if totalTime > h:
                l = midSpeed + 1
            elif totalTime <= h:
                r = midSpeed - 1
                res = min(res, midSpeed)

        return res
        








        