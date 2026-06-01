class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, elem in enumerate(nums):
            if elem == target: return idx
        return -1