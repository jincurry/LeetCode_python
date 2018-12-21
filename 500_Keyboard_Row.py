# Given a List of words, return the words that can be typed using letters of alphabet on only one
# row's of American keyboard like the image below.
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        s2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        s3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        res = []
        for w in words:
            if set(w.lower())-s1 == set() or set(w.lower())-s2 == set() or set(w.lower())-s3 == set():
                res.append(w)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))