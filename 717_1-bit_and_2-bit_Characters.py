# We have two special characters. The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last character
# must be a one-bit character or not. The given string will always end with a zero.
#
# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the last
# character is one-bit character.
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the last
#  character is NOT one-bit character.


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                if i == len(bits) - 1:
                    return True
                i += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isOneBitCharacter([1, 1, 1, 0]))
    print(solution.isOneBitCharacter([1, 0, 0]))
    print(solution.isOneBitCharacter([0, 1, 0]))
