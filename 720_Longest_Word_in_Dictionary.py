# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time
# by other words in words. If there is more than one possible answer,
# return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary.
#  However, "apple" is lexicographically smaller


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        valid = set([""])
        for word in sorted(words, key=lambda x: len(x)):
            if word[:-1] in valid:
                valid.add(word)

        return max(sorted(valid), key=lambda x: len(x))


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestWord(["w", "wo", "wor", "worl", "world"]))
    print(solution.longestWord(["a", "banana", "app", "appl", "ap", "apple", "apply"]))