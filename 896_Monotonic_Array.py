# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if
# for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.


# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return self.isIncrease(A) or self.isDecrease(A)

    def isIncrease(self, A):
        return all(A[i] - A[i + 1] <= 0 for i in range(len(A) - 1))

    def isDecrease(self, A):
        return all(A[i] - A[i + 1] >= 0 for i in range(len(A) - 1))


if __name__ == '__main__':
    result = Solution().isMonotonic([1, 2, 2, 3])
    print(result)
    result = Solution().isMonotonic([6, 5, 4, 4])
    print(result)
    result = Solution().isMonotonic([1, 2, 4, 5])
    print(result)
