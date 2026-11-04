class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap_target_idx = {}
        for idx, n in enumerate(nums):
            if target - n in hashmap_target_idx:
                return [hashmap_target_idx[target-n], idx]
            hashmap_target_idx[n] = idx