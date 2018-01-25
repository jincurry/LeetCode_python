# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next


if __name__ == '__main__':
    nums = ListNode(1)
    nums.next = ListNode(2)
    nums.next.next = ListNode(6)
    nums.next.next.next = ListNode(3)
    nums.next.next.next.next = ListNode(4)
    nums.next.next.next.next.next = ListNode(5)
    nums.next.next.next.next.next.next = ListNode(6)
    solution = Solution()
    head = solution.removeElements(nums, 6)
    while head:
        print(head.val)
        head = head.next
