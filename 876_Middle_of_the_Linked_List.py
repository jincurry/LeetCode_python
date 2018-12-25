# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_index, fast_index = head, head
        while fast_index and fast_index.next:
            fast_index = fast_index.next.next
            slow_index = slow_index.next
        return slow_index


if __name__ == '__main__':
    head = ListNode(23)
    a = ListNode(12)
    b = ListNode(24)
    c = ListNode(15)
    d = ListNode(56)
    head.next = a
    a.next = b
    b.next = c
    c.next = d
    result = Solution().middleNode(head)
    while result:
        print(result.val)
        result = result.next
