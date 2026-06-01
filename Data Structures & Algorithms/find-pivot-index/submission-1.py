class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sums = sum(nums)

        total = 0
        
        for idx, num in enumerate(nums):
        
            if total == (sums - num - total): return idx 
            total += num
        
        return -1
