class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = dict()
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if (pair in past.keys()):
                return [i,past.get(pair)]
            else: 
                past.update({num: i})
