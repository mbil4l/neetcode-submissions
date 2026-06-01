class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [1] * n
        prefix = [1] * (n + 1)
        postfix = [1] * (n + 1)

        pref = 1 
        for i in range(1, n):
            pref *= nums[i - 1]
            prefix[i] = pref

        print(prefix)

        postf = 1
        for i in range(n - 1, -1, -1):
            postf *= nums[i]
            postfix[i] = postf

        print(postfix)

        for i in range(n):
            res[i] = prefix[i] * postfix[i + 1]
        
        return res

            
            

        