class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Create a heap of (value, index) pairs
        # We need to pop the lowest value and not the index
        nums_heap = [(value, index) for index, value in enumerate(nums)]
        heapify(nums_heap)  # Turn the list into a min-heap based on value

        for _ in range(k):
            # Pop the smallest value (value, index)
            _, index = heappop(nums_heap)
            # Update the nums list in place
            nums[index] *= multiplier
            # nums[index] *= multiplier is much faster than n[i] = mult * n[i] ???
            # Push the updated value back into the heap
            heappush(nums_heap, (nums[index], index))

        return nums
# Runtime
# 0
# ms
# Beats
# 100.00%
# Analyze Complexity
# Memory
# 17.29
# MB
# Beats
# 30.05%
