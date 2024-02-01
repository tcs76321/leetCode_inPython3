class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1

        return i

# Did NOT use the editorial this time, pretty easy though obviously and didn't get the best performance but...
# Runtime 57 ms Beats 28.54% of users with Python3
# Memory 17.43 MB Beats 55.80% of users with Python3
