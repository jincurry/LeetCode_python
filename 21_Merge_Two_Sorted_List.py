# Merge two sorted linked lists and return it as a new list. The new list should
# be made by splicing together the nodes of the first two lists.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} - >{}".format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1,l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        index = current = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        # 自己测试的时候没有出现问题，但是在leetcode上无法通过
        # if l1:
        #     current.next = l1
        # if l2:
        #     current.next = l2
        # 改成这样可以通过
        current.next = l1 if l1 is not None else l2
        return index.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(0)
    l1.next = ListNode(3)
    l2 = ListNode(1)
    l2.next = ListNode(2)
    print(solution.mergeTwoLists(l1, l2))
