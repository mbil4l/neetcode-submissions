class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        cnt = 0

        for num in nums:

            if not cnt:
                candidate = num
            if num == candidate:
                cnt += 1
            else: cnt -= 1
        
        return candidate