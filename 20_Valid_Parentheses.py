# Given a string containing just the
# characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """

        :param s: str
        :return: bool
        """
        myStack = []
        characterNeed = {"(": ")", "[": "]", "{": "}"}
        for character in s:
            if character in characterNeed:
                myStack.append(character)
            elif len(myStack) == 0 or character != characterNeed[myStack.pop()]:
                return False
        return len(myStack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid('[](){}[({})]'))
    print(solution.isValid('[({)]}'))