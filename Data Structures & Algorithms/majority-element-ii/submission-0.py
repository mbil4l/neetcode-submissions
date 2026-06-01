class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)

        res = []

        for elem, freq in count.items():
            if freq > len(nums) // 3: res.append(elem)

        return res