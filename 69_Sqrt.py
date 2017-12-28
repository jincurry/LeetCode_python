# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        mid = x//2
        low, high = 1, x

        if mid*mid == x:
            return mid

        while low <= high:
            mid = low + (high - low) // 2
            if mid > x / mid:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1

if __name__ == "__main__":
    solution = Solution()
    for x in range(1,101):
        print(solution.mySqrt(x))