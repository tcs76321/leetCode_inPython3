class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        splits = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                splits += 1

        return splits

# Runtime
# 43
# ms
# Beats
# 91.76%

# Memory
# 32.19
# MB
# Beats
# 67.48%
