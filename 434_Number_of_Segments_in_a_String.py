# Count the number of segments in a string, where a segment is defined
# to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # number = s.count(' ')
        # return number + 1 if number >= 0 and len(s.strip()) != 0 else 0
        return len([i for i in s.strip().split(' ') if i])

if __name__ == '__main__':
    solution = Solution()
    print(solution.countSegments('Hello, my name is John'))
    print(solution.countSegments(''))
    print(solution.countSegments(' '))
    print(solution.countSegments('hello'))
