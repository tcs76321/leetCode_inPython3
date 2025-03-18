class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        mask = 0
        max_len = 0
        
        for right in range(len(nums)):
            while mask & nums[right] != 0:
                mask ^= nums[left]
                left += 1
            
            mask |= nums[right]
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Runtime
# 90
# ms
# Beats
# 63.72%
# Memory
# 33.66
# MB
# Beats
# 14.02%

# The following does not work:
# class Solution:
#     def longestNiceSubarray(self, nums: List[int]) -> int:
#         subarr = 0
#         counts = [0,]  # first for if will always hit so -1
#         for num in nums:
#             if (num & subarr) == 0:
#                 counts[-1] +=1
#                 subarr = num | subarr
#             else:
#                 subarr = num
#                 counts.append(1)
#
#         return max(counts) + 1
# This is because if the left most num of a given window is larger than on the right.
# In that case the count will reset to 0 instead of 
# shrinking one on the left and potentially growing 2 or more on the right missing some maxes.
# The opposite is taken care of in the working solution by shrinking to 0 one at a time, obviously.
