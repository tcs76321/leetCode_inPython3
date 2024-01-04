class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        
        count = dict()

        for num in nums:
            if (count.setdefault(num, 0)) == 0:
                count[num] = 1
                continue
            else:
                count[num] += 1

        for number, occurences in count.items():
            if occurences == 1:
                return -1
            elif occurences == 2:
                result += 1
            else:
                result += int(occurences/3)
                remainder = occurences%3
                if remainder == 0:
                    continue
                else:  # remained 1 or 2
                    result += 1
                    
        return result

# Runtime
# 573
# ms
# Beats
# 89.70%
# of users with Python3
# Memory
# 31.68
# MB
# Beats
# 14.85%
# of users with Python3
