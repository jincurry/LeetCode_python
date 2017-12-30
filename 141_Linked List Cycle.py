#  Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(1)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1
    print(solution.hasCycle(head))