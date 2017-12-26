# Write a function to find the longest common prefix string
# amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """

        :param strs: list[str]
        :return: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or strs[0][i] != string[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(['hello','helicopter', 'heaven', 'heavy']))