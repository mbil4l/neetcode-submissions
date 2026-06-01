class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elemFrequency = Counter(nums)
        
        minheap = []

        for num, freq in elemFrequency.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (freq, num))
            else:
                if freq <= minheap[0][0]:
                    continue
                else:
                    heapq.heapreplace(minheap, (freq, num))
        
        return [elem for freq, elem in minheap]
        
        