class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for idx, num in enumerate(nums):

            if idx >= 1 and num == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1

            while l < r:
                
                target = num + nums[l] + nums[r] 

                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1

        
        return res
