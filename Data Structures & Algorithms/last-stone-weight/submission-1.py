class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) <= 1: return stones[0]

        maxheap = []

        for stone in stones: heapq.heappush(maxheap, -stone)

        while len(maxheap) > 1:

            heapq.heappush(maxheap, heapq.heappop(maxheap) - heapq.heappop(maxheap))

        return -maxheap[0] 


            


