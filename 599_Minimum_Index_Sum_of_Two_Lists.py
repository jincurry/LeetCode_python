# # Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
# #  represented by strings.
# #
# # You need to help them find out their common interest with the least list index sum.
# # If there is a choice tie between answers, output all of them with no order requirement.
# #  You could assume there always exists an answer.
#
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        for i, s in enumerate(list1):
            dict1[s] = i
        result = []
        min_sum = float('inf')
        for j, k in enumerate(list2):
            if j > min_sum:
                break
            if k in dict1:
                if j + dict1[k] < min_sum:
                    result = [k]
                    min_sum = j + dict1[k]
                elif j + dict1[k] == min_sum:
                    result.append(k)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti",
                                                                                        "The Grill at Torrey Pines",
                                                                                        "Hungry Hunter Steakhouse",
                                                                                        "Shogun"]))
