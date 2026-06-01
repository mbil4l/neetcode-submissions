class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1

        for r in nums[1:]:

            if r == nums[l - 1]:
                continue
            else:
                nums[l] = r
                l += 1
        return l

        


            

            


