class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        total = 0
        for num in nums:
            total += num
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)