class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = True
        result = 0
        streak = 0
        prev = -1
        for num in nums:
            if num > prev:
                if increasing:
                    streak += 1
                    prev = num
                    result = max(streak, result)
                else:  # broken subseq
                    streak = 2
                    result = max(streak, result)
                    prev = num
                    increasing = True  # increasing was false
            elif num < prev:
                if not increasing:
                    streak += 1
                    prev = num
                    result = max(streak, result)
                else:  # broken subseq
                    streak = 2
                    result = max(streak, result)
                    prev = num
                    increasing = False
            else:  # num == prev
                streak = 1
                increasing = False  # TODO: not decreasing though?
                result = max(streak, result)  # TODO: unnecessary??
            
        return result

# Runtime
# 0
# ms
# Beats
# 100.00%
# Memory
# 17.68
# MB
# Beats
# 67.96%
