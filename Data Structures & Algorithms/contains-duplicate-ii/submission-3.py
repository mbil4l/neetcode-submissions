class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # for n in range(len(nums) - k + 1):
        
        
        window = set()
        cur, l = 0, 0
        
        for r in range(len(nums)):
            if nums[r] in window: return True
            window.add(nums[r])

            if len(window) > k:
                window.remove(nums[l])
                l += 1
        return False
