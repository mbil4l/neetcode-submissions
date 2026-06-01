class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elemFrequency = Counter(nums)
        
        mxheap = []

        for num, freq in elemFrequency.items():
            heapq.heappush(mxheap, (-freq, num))
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(mxheap)[1])
        
        return res