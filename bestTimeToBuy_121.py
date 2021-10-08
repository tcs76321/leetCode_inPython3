class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = -1
        low = 10001
        profit = 0
        for i in prices:
            if i < low:
                low = i
            elif i - low > profit:
                profit = i - low
        return profit
