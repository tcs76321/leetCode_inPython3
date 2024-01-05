class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_nums = len(nums)
        
        result = []

        result.append(nums[0])

        for i in range(1, length_nums):
            n = nums[i]
            if n > result[-1]:
                result.append(n)
            else:
                low = 0
                high = len(result) - 1

                while low < high:
                    mid = low + (high - low) // 2
                    if result[mid] < n:
                        low = mid + 1
                    else:
                        high = mid

                result[low] = n

        return len(result)

# Thank you GeeksForGeeks!
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
