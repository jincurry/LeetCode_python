# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the
# number and for the multiples of five output “Buzz”. For numbers which are
# multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                result.append('FizzBuzz')
            elif x % 3 == 0:
                result.append('Fizz')
            elif x % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(x))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.fizzBuzz(15))