class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        cnt = Counter(nums)

        if cnt[target] > len(nums) // 2: return True

        return False
        