class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lookup = set(nums)
        
        longest = 0
        
        for num in nums:
            current = 1
            if num - 1 not in lookup:
                while num + 1 in lookup: 
                    current += 1
                    num += 1
                longest = max(current, longest)
        
        return longest



