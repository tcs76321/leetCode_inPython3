class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        result = 0
        length = 0 - len(s)

        while s[i] == ' ':
            i -= 1

        while s[i] != ' ':
            i -= 1
            result += 1
            if i < length:
                return result

        return result
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         result = len(s.rsplit(' ', 1)[-1])
#         i = -1
#         while result == 0:
#             i -= 1
#             result = len(s.rsplit(' ')[i])
#         return result
