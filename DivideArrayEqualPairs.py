class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        totals = defaultdict(int)
        for num in nums:
            totals[num] += 1
        for key, value in totals.items():
            if value % 2 == 1:
                return False
        return True


# Runtime
# 3
# ms
# Beats
# 70.86%
# Analyze Complexity
# Memory
# 18.09
# MB
# Beats
# 24.91%


# class Solution:
#     def divideArray(self, nums: List[int]) -> bool:
#         nums.sort()
#         prev = 0
#         count = 0
#         for num in nums:
#             if num != prev:
#                 # check for a set of nums being odd
#                 if count > 0 and (count % 2) == 1:
#                     return False
#                 # otherwise reset
#                 prev = num
#                 count = 1
#             else:  # num == prev
#                 count += 1
#         return True
# Runtime
# 4
# ms
# Beats
# 42.68%
# Analyze Complexity
# Memory
# 18.05
# MB
# Beats
# 24.91%
