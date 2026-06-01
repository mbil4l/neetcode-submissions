class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return nums[0]
        
        cursum, maxsum = 0, float('-inf')
        
        for n in nums:

            cursum = max(cursum, 0) + n
            maxsum = max(maxsum, cursum)
        
        return maxsum

