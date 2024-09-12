class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for word in words:
            result += 1
            for letter in word:
                if letter not in allowed:
                    result -= 1
                    break

        return result

# Runtime 208ms Beats 66.67%
# O(N*M)

# Memory 18.56MB Beats 40.73%
# O(1)
