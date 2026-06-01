class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res, curr = [], []


        def kSum(k, idx, target):

            if k == 2:
                
                l, r = idx, len(nums) - 1
                
                while l < r:
                    
                    s = nums[l] + nums[r]

                    if s > target: r -= 1
                    elif s < target: l += 1
                    else:
                        res.append(curr + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
            
            else:

                for i in range(idx, len(nums) - k + 1):
                    
                    if i > idx and nums[i] == nums[i - 1]:
                        continue

                    curr.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    curr.pop()
        
        kSum(4, 0, target)
        return res
