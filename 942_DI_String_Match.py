# Given a string S that only contains "I" (increase) or "D" (decrease),
#  let N = S.length.

# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]


# Example 1:

# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:

# Input: "III"
# Output: [0,1,2,3]
# Example 3:

# Input: "DDI"
# Output: [3,2,0,1]


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        res = []
        number_of_I, number_of_D = 0, N
        for s in S:
            if s == 'I':
                res.append(number_of_I)
                number_of_I += 1
            else:
                res.append(number_of_D)
                number_of_D -= 1
        res.append(number_of_I)
        return res


if __name__ == "__main__":
    result = Solution().diStringMatch(S='DDI')
    print(result)