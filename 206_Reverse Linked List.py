# Reverse a singly linked list.


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = Solution().reverseList(head)
    while result:
        print(result.val)
        result = result.next
