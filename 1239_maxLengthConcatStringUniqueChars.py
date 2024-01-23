class Solution:
    def dfs(self, arr: List[str], pos: int, res: str) -> int:
        # use set() to check for duplicates, if we found any then return 0 because we want only unique
        if len(res) != len(set(res)):
            return 0

        best = len(res) # initially 0 when first called below
        # here is the magic, we loop 
        for i in range(pos, len(arr)):
            best = max(
                best,
                self.dfs(arr, i+1, res+arr[i]) # this can come up with duplicates, but will be handled above
                # we break out of 0 vals in best/rest by passing res+arr[i] recursively
                # pos/i start out as 0 because we use it below that way, this makes sure we don't miss the first str in arr
            ) # when something has duplicate as determined above it will give 0 here and always not become best

        return best


    def maxLength(self, arr: List[str]) -> int:
        return self.dfs(arr, 0, "")


# ** Had to use the editorial on this. I do think I understand the idea of it though. Not going to delve into the optimization however.
