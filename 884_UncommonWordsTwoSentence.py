class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(" ")
        words2 = s2.split(" ")

        all_words = words1 + words2

        result = []
        common = []

        for word in all_words:
            if word in result:
                common.append(word)
                result.remove(word)
            elif word in common:
                continue
            else:  # word is not already in result or a previous common
                result.append(word)

        return result

# Runtime
# 34
# ms
# Beats
# 69.44%
# Analyze Complexity
# Memory
# 16.58
# MB
# Beats
# 44.21%
