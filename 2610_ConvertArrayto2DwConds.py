class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []

        number_dict = dict()

        max_count = 0
        max_number = 0

        for num in nums:
            number_dict[num] = number_dict.get(num, 0) + 1
            if max_count < number_dict[num]:
                max_count = number_dict[num]
                max_number = num
        
        for i in range(0, max_count):
            result.append([max_number,])
        
        del number_dict[max_number]

        for key, value in number_dict.items():
            for i in range(0, value):
                result[i].append(key)

        return result

# Runtime
# 49
# ms
# Beats
# 94.51%
# of users with Python3
# Memory
# 17.48
# MB
# Beats
# 19.51%
# of users with Python3
