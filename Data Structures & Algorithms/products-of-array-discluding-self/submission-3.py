class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        prefix = res.copy()
        postfix = res.copy()

        pref = 1
        for i in range(1, len(nums)):
            pref *= nums[i - 1]
            prefix[i] = pref

        postf = 1
        for i in range(len(nums) - 2, -1, -1):
            postf *= nums[i + 1]
            postfix[i] = postf

        print(prefix, postfix)
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        return res