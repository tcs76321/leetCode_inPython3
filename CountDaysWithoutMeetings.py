class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        result = 0
        last_end = 0
        meetings.sort()

        for start, end in meetings:
            if start > last_end:
                result += start - last_end - 1
            if end > last_end:
                last_end = end

        result += days - last_end

        return result

# Runtime
# 188
# ms
# Beats
# 48.60%
# Memory
# 52.98
# MB
# Beats
# 31.30%
