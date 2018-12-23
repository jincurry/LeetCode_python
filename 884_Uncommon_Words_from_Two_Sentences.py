# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists
# only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words.

# You may return the list in any order.


# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        split_A = A.split(' ')
        split_B = B.split(' ')
        counter_A = Counter(split_A)
        counter_B = Counter(split_B)
        result = []
        for each in split_A:
            if each not in split_B and counter_A[each] == 1:
                result.append(each)
        for each in split_B:
            if each not in split_A and counter_B[each] == 1:
                result.append(each)
        return result

    def uncommonFromSentences2(self, A, B):
        counter = Counter(A.split() + B.split())
        return [word for word in counter if counter[word] == 1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.uncommonFromSentences(
        A="this apple is sweet", B="this apple is sour")
    print(result)
    result = solution.uncommonFromSentences2(A="apple apple", B="banana")
    print(result)
