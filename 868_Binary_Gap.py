# Given a positive integer N, find and return the longest distance between two consecutive 1's
# in the binary representation of N.

# If there aren't two consecutive 1's, return 0.


# Example 1:

# Input: 22
# Output: 2
# Explanation:
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# Example 2:

# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
# Example 3:

# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        string = bin(N)[2:]
        left = -1
        res = 0
        for index, value in enumerate(string):
            if value == '1':
                if left != -1:
                    res = max(res, index - left)
                left = index
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.binaryGap(5)
    print(result)
