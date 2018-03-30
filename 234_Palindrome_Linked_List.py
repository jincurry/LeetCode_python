# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    print(solution.isPalindrome(head))