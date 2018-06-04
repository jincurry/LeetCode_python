# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions
#  of every large group.
#
# The final answer should be in lexicographic order.

# Example 1:
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        result = []
        if len(set(S)) == 1 and len(S) > 3:
            return [[0, len(S) - 1]]
        if len(S) == 1:
            return []
        while i < len(S) - 1:
            if S[i+1] == S[i]:
                i += 1
                if i == len(S) - 1 and S[i] == S[i-1]:
                    if i -j >= 2:
                        result.append([j, i])
                else:
                    continue
            else:
                i += 1
                if i - j >= 3:
                    result.append([j, i-1])
                j = i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.largeGroupPositions('abbxxxxzzy'))
    print(solution.largeGroupPositions("abc"))
    print(solution.largeGroupPositions("abcdddeeeeaabbbcd"))
    print(solution.largeGroupPositions("aaa"))
    print(solution.largeGroupPositions("aaab"))
    print(solution.largeGroupPositions("a"))
    print(solution.largeGroupPositions("aa"))
    print(solution.largeGroupPositions("babaaaabbb"))
