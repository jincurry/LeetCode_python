# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and
# only if the given words are sorted lexicographicaly in this alien language.


# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.)
# According to lexicographical rules "apple" > "app", because 'l' > '∅',
# where '∅' is defined as the blank character which is less than any other character (More info).

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {c: i for i, c in enumerate(order)}
        d['#'] = -1
        max_length = max(map(len, words))
        temp = []
        for each in words:
            if len(each) < max_length:
                each += '#' * (max_length - len(each))
            temp.append(each)
        for i in range(len(words) - 1):
            pre, after = temp[i], temp[i + 1]
            for j in range(max_length):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] == d[after[j]]:
                    continue
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.isAlienSorted(words=['hello', 'leetcode'],
                                    order='hlabcdefgijkmnopqrstuvwxyz')
    print(result)
    result = solution.isAlienSorted(
        words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
    print(result)
    result = solution.isAlienSorted(
        words=['apple', 'app'], order='abcdefghijklmnopqrstuvwxyz')
    print(result)
