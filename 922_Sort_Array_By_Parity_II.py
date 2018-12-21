# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers
# are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.


# Example 1:

# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        odd = list(filter(lambda x: x % 2 != 0, A))
        even = list(filter(lambda x: x % 2 == 0, A))
        for each in zip(even, odd):
            for i in each:
                result.append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.sortArrayByParityII([4, 2, 1, 7])
    print(result)
