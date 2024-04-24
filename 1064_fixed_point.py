class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        length = len(arr)

        for i in range(0, length):
            if arr[i] == i:
                return i
            else:
                i += 1

        return -1
