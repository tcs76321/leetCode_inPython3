class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        chars = set()

        for right in range(len(s)):
            right_char = s[right]

            while right_char in chars:
                left_char = s[left]
                chars.remove(left_char)
                left += 1

            chars.add(right_char)

            max_len = max(max_len, right - left + 1)

        return max_len
