# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting
#  from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made,
#  return an empty string.


# Example 1:

# Input: [1,2,3,4]
# Output: "23:41"
# Example 2:

# Input: [5,5,5,5]
# Output: ""

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h // 10, h % 10, m // 10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) + ":" + str(t[2]) + str(t[3])
        return ""


if __name__ == "__main__":
    result = Solution()
    print(result.largestTimeFromDigits([1, 2, 3, 4]))