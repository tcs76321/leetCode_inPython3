class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        
        nextAddition = -1
        
        l = len(nums)
        
        for iterator in range(1, l+1):
            for i in nums:
                if (i % 10) > nextAddition:
                    nextAddition = i
            res += str(i)
            nums.remove(i)
            
        return res
