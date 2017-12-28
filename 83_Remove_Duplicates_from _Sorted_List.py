# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = head
        while i:
            j = i.next
            while j and j.val == i.val:
                j = j.next
            i.next = j
            i = j
        return head

if __name__ == "__main__":
    solution = Solution()
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print(solution.deleteDuplicates(head).val)
    print(solution.deleteDuplicates(head).next.val)
    print(solution.deleteDuplicates(head).next.next.val)