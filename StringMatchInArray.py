class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                elif word1 in word2:
                    result.append(word1)
                    break

        return result

# Runtime
# 0
# ms
# Beats
# 100.00%
# Memory
# 17.48
# MB
# Beats
# 38.61%
