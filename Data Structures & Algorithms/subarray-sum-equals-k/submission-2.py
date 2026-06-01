class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        total = 0
        for num in nums:
            total += num
            if total - k in prefixCount.keys():
                res += prefixCount[total - k]
            prefixCount[total] += 1
        return res

            
       
       

       

