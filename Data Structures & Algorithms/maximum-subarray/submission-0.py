class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        add, res = 0, nums[0]   

        for n in nums:
            add += n 
            res = max(res, add)
            add = max(add, 0)
        return res
        