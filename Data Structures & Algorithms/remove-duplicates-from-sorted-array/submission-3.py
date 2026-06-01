class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 1, 1

        while r < len(nums):

            while r < len(nums) and nums[r] == nums[l - 1]:
                r += 1
            else:
                if r < len(nums):
                    nums[l] = nums[r]
                    l += 1
            r += 1
        
        return l
            

            


